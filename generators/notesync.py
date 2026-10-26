import subprocess, sys, time, json, urllib.parse
from playwright.sync_api import sync_playwright
src=open('tools/e2e.py').read(); exec(src[src.index('def solve'):src.index('try:')])
D='/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/gt2'
srv=subprocess.Popen([sys.executable,'-m','http.server','8793','-d',D],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
STORE={}; ROSTER={'김민준':'4821'}; LOG=[]
nc=lambda c: ''.join(ch for ch in str(c) if ch.isdigit()).lstrip('0')
def handler(route, req):
    q=urllib.parse.parse_qs(urllib.parse.urlparse(req.url).query, keep_blank_values=True); H={'Access-Control-Allow-Origin':'*','Content-Type':'application/json'}
    if req.method=='POST':
        d=json.loads(req.post_data or '{}')
        for n in d.get('notes',[]):
            k=n['name']+'|'+n['unit']+'|'+n['id']; LOG.append(('del' if n.get('del') else 'put',k))
            if n.get('del'): STORE.pop(k,None)
            elif k not in STORE or json.loads(STORE[k]['data'])['at']<=n['at']: STORE[k]=n
        return route.fulfill(status=200, body='ok')
    if 'check' in q:
        n=q['name'][0]; ok=n in ROSTER and nc(ROSTER[n])==nc(q.get('code',[''])[0])
        return route.fulfill(status=200, body=json.dumps({'gate':True,'ok':ok,'why':'' if ok else 'code'}), headers=H)
    if 'notes' in q:
        n=q['name'][0]; ok=n in ROSTER and nc(ROSTER[n])==nc(q.get('code',[''])[0])
        out=[v['data'] for k,v in STORE.items() if k.startswith(n+'|'+q['unit'][0]+'|')] if ok else []
        return route.fulfill(status=200, body=json.dumps({'ok':ok,'notes':out}), headers=H)
    route.fulfill(status=200, body='작동 중', headers={'Access-Control-Allow-Origin':'*'})
R=[]
def chk(n,c): R.append(bool(c)); print(('PASS ' if c else 'FAIL ')+n)
def enter(pg):
    pg.goto('http://localhost:8793/u/?test'); pg.wait_for_timeout(900)
    pg.fill('#nm','김민준'); pg.fill('#pc','4821'); pg.click('#nameform [type=submit]'); pg.wait_for_timeout(900)
try:
  with sync_playwright() as p:
    b=p.chromium.launch()
    A=b.new_context(viewport={'width':390,'height':844}); pa=A.new_page(); pa.route('**/script.google.com/**', handler)
    enter(pa); chk('A 기기 들어감', pa.locator('.notecard').count()==1)
    pa.locator('[data-go="0"]').first.click(); pa.click('#gostart')
    solve(pa, True); pa.click('#nx'); solve(pa, False); pa.click('#conf'); pa.click('#nx'); solve(pa, False); pa.click('#conf'); pa.click('#conf')
    pa.wait_for_timeout(1500)
    print('  sheet store:', len(STORE), LOG)
    chk('시트에 2개 저장 (틀림 1 + 헷갈림 1, 취소한 건 지움)', len(STORE)==2)
    # B 기기: 새 기기, 같은 이름·코드
    B=b.new_context(viewport={'width':390,'height':844}); pb=B.new_page(); pb.route('**/script.google.com/**', handler)
    enter(pb); pb.wait_for_timeout(1500)
    t=pb.inner_text('.notecard'); print('  B card:', t.replace('\n',' | '))
    chk('B 기기에서도 같은 오답 노트 2개', '모은 문제 2' in t)
    pb.click('[data-note="*"]'); 
    while pb.evaluate('__dbg()')['phase']!='summary': solve(pb, False); pb.click('#nx')
    pb.click('#back'); pb.wait_for_timeout(1500)
    oks=[json.loads(v['data'])['ok'] for v in STORE.values()]; print('  store ok flags', oks)
    chk('B에서 다시 맞힌 결과가 시트에 반영', all(oks))
    # A 다시 열기 → B의 결과가 내려옴
    pa.reload(); pa.wait_for_timeout(1500)
    if pa.locator('[data-who]').count(): pa.click('[data-who="김민준"]'); pa.wait_for_timeout(1500)
    t=pa.inner_text('.notecard'); print('  A card:', t.replace('\n',' | '))
    chk('A 기기에도 B의 결과(남은 0)가 반영', '남은 문제 0' in t)
    # 다른 사람이 이름만 알고 코드 틀리면 못 받음
    C=b.new_context(); pc=C.new_page(); pc.route('**/script.google.com/**', handler)
    pc.goto('http://localhost:8793/u/?test'); pc.wait_for_timeout(900); pc.fill('#nm','김민준'); pc.fill('#pc','1111'); pc.click('#nameform [type=submit]'); pc.wait_for_timeout(900)
    print('  C screen:', pc.inner_text('#app')[:300].replace('\n',' | ')); chk('코드 틀리면 들어가지 못함', pc.locator('.notecard').count()==0)
    b.close()
finally: srv.terminate()
print('ALL OK' if all(R) else 'SOME FAILED')
