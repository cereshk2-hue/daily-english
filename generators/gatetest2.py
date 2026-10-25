import subprocess, sys, time, json, re, urllib.parse
from playwright.sync_api import sync_playwright
D='/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/gt'
srv=subprocess.Popen([sys.executable,'-m','http.server','8772','-d',D],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
MODE={'m':'old'}; ROWS=[]  # (name, code, book)
nc=lambda c: ''.join(ch for ch in str(c) if ch.isdigit()).lstrip('0')
nb=lambda t: re.sub(r'[\s()·.\-]','',str(t).lower())
def bookOk(cell, school):
    parts=[nb(x) for x in re.split(r'[,/\n]',cell) if nb(x)]
    return not parts or any(x in nb(school) or nb(school) in x for x in parts)
def handler(route, req):
    q=urllib.parse.parse_qs(urllib.parse.urlparse(req.url).query)
    if req.method=='POST': return route.fulfill(status=200, body='ok')
    if MODE['m']=='offline': return route.abort()
    if 'check' not in q or MODE['m']=='old': return route.fulfill(status=200, body='작동 중', headers={'Access-Control-Allow-Origin':'*'})
    n=q.get('name',[''])[0]; c=nc(q.get('code',[''])[0]); sc=q.get('school',[''])[0]
    rows=[r for r in ROWS if r[0]]; res={'gate':bool(rows),'ok':False,'why':''}
    if rows:
        mine=[r for r in rows if n and c and r[0]==n and nc(r[1])==c]
        if not mine: res['why']='code'
        elif any(bookOk(r[2],sc) for r in mine): res['ok']=True
        else: res['why']='unit'
    route.fulfill(status=200, body=json.dumps(res), headers={'Access-Control-Allow-Origin':'*','Content-Type':'application/json'})
R=[]
def chk(name, cond): R.append(bool(cond)); print(('PASS ' if cond else 'FAIL ')+name)
def state(pg):
    if pg.locator('.bnav').count(): return 'home'
    if pg.locator('#recheck').count(): return 'unit'
    if pg.locator('#passform #pc').count(): return 'code'
    if pg.locator('#nameform').count(): return 'name'
    if pg.locator('#passform').count(): return 'checking'
    return '?'
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844})
    pg.route('**/script.google.com/**', handler)
    A='http://localhost:8772/u/'; B='http://localhost:8772/v/'
    MODE['m']='new'; ROWS[:]=[('김민준','4821','중2 비상'),('혜연쌤','1004','')]
    pg.goto(A); pg.wait_for_timeout(1000)
    chk('1 명단 켜짐 → 이름+코드 칸', pg.locator('#nameform #pc').count()==1)
    pg.fill('#nm','김민준'); pg.fill('#pc','4821'); pg.click('#nameform [type=submit]'); pg.wait_for_timeout(700)
    chk('2 중2 비상 링크: "중2 비상"으로 적힌 학생 들어감 ('+state(pg)+')', state(pg)=='home')
    pg.goto(B); pg.wait_for_timeout(1200)
    chk('3 중3 지학사 링크: 코드 다시 안 묻고 "열리지 않은 과제" ('+state(pg)+')', state(pg)=='unit')
    pg.screenshot(path=D+'/../gate_unit.png')
    ROWS.append(('김민준','4821','중3 지학사(민찬규)'))
    pg.click('#recheck'); pg.wait_for_timeout(800)
    chk('4 선생님이 한 줄 추가 → 다시 확인하기 → 들어감 ('+state(pg)+')', state(pg)=='home')
    ROWS[:]=[('김민준','4821','중2 비상(황종배), 중3 지학사'),('혜연쌤','1004','')]
    pg.reload(); pg.wait_for_timeout(1000); chk('5 쉼표로 두 교재 → 지학사 열림 ('+state(pg)+')', state(pg)=='home')
    pg.goto(A); pg.wait_for_timeout(1000); chk('6 쉼표로 두 교재 → 비상 열림 ('+state(pg)+')', state(pg)=='home')
    ROWS[:]=[('김민준','4821','중2 동아'),('혜연쌤','1004','')]
    pg.reload(); pg.wait_for_timeout(1200); chk('7 교재를 동아로 바꾸면 비상 링크 막힘 ('+state(pg)+')', state(pg)=='unit')
    pg.click('#notme'); pg.wait_for_timeout(300)
    pg.fill('#nm','혜연쌤'); pg.fill('#pc','1004'); pg.click('#nameform [type=submit]'); pg.wait_for_timeout(700)
    chk('8 교재 비운 선생님 → 들어감 ('+state(pg)+')', state(pg)=='home')
    pg.goto(B); pg.wait_for_timeout(1000)
    if pg.locator('[data-who="혜연쌤"]').count(): pg.click('[data-who="혜연쌤"]'); pg.wait_for_timeout(1000)
    chk('9 선생님 다른 교재도 들어감 ('+state(pg)+')', state(pg)=='home')
    ROWS[:]=[('혜연쌤','1004','')]
    pg.goto(A); pg.wait_for_timeout(800)
    if pg.locator('[data-who="김민준"]').count(): pg.click('[data-who="김민준"]'); pg.wait_for_timeout(1200)
    chk('10 명단에서 지운 김민준 → 코드 화면 ('+state(pg)+')', state(pg)=='code')
    MODE['m']='offline'; pg.goto(B); pg.wait_for_timeout(800)
    if pg.locator('[data-who="혜연쌤"]').count(): pg.click('[data-who="혜연쌤"]'); pg.wait_for_timeout(800)
    chk('11 인터넷 끊겨도 확인된 교재는 공부 가능 ('+state(pg)+')', state(pg)=='home')
    MODE['m']='new'; ROWS[:]=[]
    pg.goto(A); pg.wait_for_timeout(800)
    if pg.locator('[data-who="김민준"]').count(): pg.click('[data-who="김민준"]'); pg.wait_for_timeout(1200)
    chk('12 명단 비우면 다시 누구나 ('+state(pg)+')', state(pg)=='home')
    b.close()
finally: srv.terminate()
print('ALL OK' if all(R) else 'SOME FAILED')
