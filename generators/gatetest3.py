import subprocess, sys, time, json, re, urllib.parse
from playwright.sync_api import sync_playwright
D='/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/gt'
srv=subprocess.Popen([sys.executable,'-m','http.server','8794','-d',D],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
ROWS=[]  # [name, code, book, memo]
nc=lambda c: ''.join(ch for ch in str(c) if ch.isdigit()).lstrip('0')
nb=lambda t: re.sub(r'[\s()·.\-]','',str(t).lower())
def bookOk(cell, school):
    parts=[nb(x) for x in re.split(r'[,/\n]',cell) if nb(x)]
    return not parts or any(x in nb(school) or nb(school) in x for x in parts)
def handler(route, req):
    q=urllib.parse.parse_qs(urllib.parse.urlparse(req.url).query, keep_blank_values=True); H={'Access-Control-Allow-Origin':'*','Content-Type':'application/json'}
    if req.method=='POST': return route.fulfill(status=200, body='ok')
    if 'check' in q:
        n=q['name'][0]; c=nc(q['code'][0]); raw=re.sub(r'\D','',q['code'][0]); res={'gate':True,'ok':False,'why':''}
        mine=[r for r in ROWS if n and r[0]==n]
        if mine:
            if any(re.search('그만|차단|퇴원|정지', r[3]) for r in mine): res['why']='blocked'
            else:
                ok=[r for r in mine if c and nc(r[1])==c]
                if not ok: res['why']='code'
                elif any(bookOk(r[2], q['school'][0]) for r in ok): res['ok']=True
                else: res['why']='unit'
        elif q.get('reg',[''])[0]=='1' and re.fullmatch('[가-힣]{2,5}',n) and re.fullmatch(r'\d{4}',raw):
            ROWS.append([n,raw,'','자동 등록']); res['ok']=True; res['isNew']=True
        else: res['why']='new' if n else 'code'
        return route.fulfill(status=200, body=json.dumps(res), headers=H)
    if 'notes' in q: return route.fulfill(status=200, body=json.dumps({'ok':True,'notes':[]}), headers=H)
    route.fulfill(status=200, body='작동 중', headers={'Access-Control-Allow-Origin':'*'})
R=[]
def chk(n,c): R.append(bool(c)); print(('PASS ' if c else 'FAIL ')+n)
def state(pg):
    if pg.locator('.bnav').count(): return 'home'
    if pg.locator('#recheck').count(): return 'unit'
    if pg.locator('#passform #pc').count(): return 'code'
    if pg.locator('#nameform').count(): return 'name'
    if pg.locator('#passform').count(): return 'msg:'+pg.inner_text('#passform')[:30]
    return '?'
def newctx(b):
    c=b.new_context(viewport={'width':390,'height':844}); pg=c.new_page(); pg.route('**/script.google.com/**', handler); return pg
try:
  with sync_playwright() as p:
    b=p.chromium.launch()
    A=newctx(b); A.goto('http://localhost:8794/u/'); A.wait_for_timeout(1000)
    chk('처음 화면: 이름+코드 칸만, 학습 화면 숨김', A.locator('#nameform #pc').count()==1 and A.locator('.hero').count()==0)
    A.fill('#nm','김민준'); A.fill('#pc','12'); A.click('#nameform [type=submit]'); A.wait_for_timeout(300)
    chk('코드 4자리 아니면 안내', '4자리' in A.inner_text('#nmbad'))
    A.fill('#pc','4821'); A.click('#nameform [type=submit]'); A.wait_for_timeout(800)
    chk('새 이름 + 코드 → 자동 등록되고 들어감 (명단 %s)'%ROWS, state(A)=='home' and ROWS==[['김민준','4821','','자동 등록']])
    chk('처음 등록하면 코드 알림 카드', A.locator('#newcode').count()==1 and '4821' in A.inner_text('#newcode'))
    A.screenshot(path=D+'/../reg_home.png'); A.click('#codeok'); A.wait_for_timeout(200)
    chk('기억했어요 → 카드 사라짐', A.locator('#newcode').count()==0)
    B=newctx(b); B.goto('http://localhost:8794/u/'); B.wait_for_timeout(1000)
    B.fill('#nm','김민준'); B.fill('#pc','1111'); B.click('#nameform [type=submit]'); B.wait_for_timeout(600)
    chk('남이 같은 이름 + 다른 코드 → 막힘', state(B)=='name' and '이미 등록' in B.inner_text('#nmbad'))
    B.fill('#pc','4821'); B.click('#nameform [type=submit]'); B.wait_for_timeout(800)
    chk('다른 기기에서 같은 이름+코드 → 들어감', state(B)=='home' and len(ROWS)==1)
    ROWS[0][3]='그만둠 10/26'
    B.goto('http://localhost:8794/v/'); B.wait_for_timeout(1200)
    if B.locator('[data-who="김민준"]').count(): B.click('[data-who="김민준"]'); B.wait_for_timeout(1200)
    chk('메모에 그만둠 → 다른 교재도 막힘 (%s)'%state(B), state(B).startswith('msg:지금은'))
    A.reload(); A.wait_for_timeout(1500)
    if A.locator('[data-who="김민준"]').count(): A.click('[data-who="김민준"]'); A.wait_for_timeout(1500)
    chk('기존 기기도 다음에 열 때 막힘 (%s)'%state(A), state(A).startswith('msg:지금은'))
    A.click('#notme'); A.wait_for_timeout(200); A.fill('#nm','김민준'); A.fill('#pc','4821'); A.click('#nameform [type=submit]'); A.wait_for_timeout(600)
    chk('그만둔 이름은 다시 등록도 안 됨', state(A)=='name' and '학습할 수 없어요' in A.inner_text('#nmbad') and len(ROWS)==1)
    ROWS.append(['이서연','7777','중3 지학사','']); C=newctx(b); C.goto('http://localhost:8794/u/'); C.wait_for_timeout(1000)
    C.fill('#nm','이서연'); C.fill('#pc','7777'); C.click('#nameform [type=submit]'); C.wait_for_timeout(800)
    chk('선생님이 교재를 정한 학생은 그 교재만 (%s)'%state(C), state(C)=='unit')
    b.close()
finally: srv.terminate()
print('ALL OK' if all(R) else 'SOME FAILED')
