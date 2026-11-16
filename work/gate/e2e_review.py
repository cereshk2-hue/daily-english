# 오답 학습 검수: DAY마다 단계별 첫 문제를 일부러 틀리고(한 판은 3번 실패) → 결과 → '오답 학습' → 다 맞혀서 끝까지 → 오답 노트도 풀기
import subprocess, time, sys, json
from playwright.sync_api import sync_playwright
FOLDER, PORT, DAYS = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(',')]
srv=subprocess.Popen([sys.executable,'-m','http.server',PORT,'-d','/home/claude/proj/dist/github/'+FOLDER],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
errs=[]
def gate_choose(pg,q,wrong=False):
    k=0
    for pi,p in enumerate(q['parts']):
        for si,sg in enumerate(p['segs']):
            if 'opts' not in sg: continue
            o=sg['opts'].index(sg['ans'])
            if wrong and k==0: o=1-o
            pg.locator('.gb[data-g="%d:%d"] .gopt[data-o="%d"]'%(pi,si,o)).click(); k+=1
def gate_review(pg,q):
    for g in pg.locator('.gb').all():
        pi,si=map(int,g.get_attribute('data-g').split(':')); sg=q['parts'][pi]['segs'][si]
        g.locator('.gopt[data-o="%d"]'%sg['opts'].index(sg['ans'])).click()
    assert pg.locator('#gre').is_enabled(), 'gre off'; pg.click('#gre'); time.sleep(.3)
def solve(pg, wrong=False):
    rs=pg.evaluate('__dbg()'); q=rs['qs'][rs['qi']]; t=q['t']
    if t=='gate':
        if wrong:
            for _ in range(3):
                q=pg.evaluate('__dbg()')['qs'][rs['qi']]; gate_choose(pg,q,True); pg.click('#gchk'); time.sleep(.3)
            gate_review(pg, pg.evaluate('__dbg()')['qs'][rs['qi']])
        q=pg.evaluate('__dbg()')['qs'][rs['qi']]
        st=pg.evaluate("[...document.querySelectorAll('.gopt')].slice(0,4).map(x=>x.className+(x.disabled?'(off)':''))")
        if any('(off)' in x for x in st): print('   !! 보기 꺼짐', rs['qi'], q.get('phase'), q.get('passed'), q.get('round'), st)
        gate_choose(pg,q); pg.click('#gchk'); return t
    if wrong and t in ('choice','pick','tf','multi'):
        if t=='tf': pg.locator('.opt[data-v="%d"]'%(1-int(q['ans']))).click()
        elif t=='multi': pg.locator('.opt').nth(next(i for i,o in enumerate(q['opts']) if o not in q['ans'])).click(); pg.click('#mok')
        else: pg.locator('.opt').nth(next(i for i,o in enumerate(q['opts']) if o!=q['ans'])).click()
        return t+'(x)'
    if t in('choice','pick'): pg.locator('.opt').nth(q['opts'].index(q['ans'])).click()
    elif t=='multi':
        for a in q['ans']: pg.locator('.opt').nth(q['opts'].index(a)).click(); time.sleep(0.05)
        pg.click('#mok')
    elif t=='tf': pg.locator('.opt[data-v="%d"]'%int(q['ans'])).click()
    elif t=='verb': pg.fill('#vin', q['a'][0]); pg.click('#vf button')
    elif t in('insert','odd'): pg.locator('#qcard [data-m="%d"]'%q['ans']).click()
    elif t=='error': pg.locator('.mark[data-m="%d"]'%q['w']).click()
    elif t in('order','scramble'):
        for j in range(q.get('need') or len(q['pool'])): pg.locator('#pool .chip[data-j="%d"]'%j).click()
        pg.click('#chk')
    elif t=='hunt':
        for i,w in enumerate(q['toks']):
            if w.get('e') is not None: pg.locator('.hw[data-h="%d"]'%i).click()
        pg.click('#hchk')
        for j,e in enumerate(q['errs']): pg.fill('[data-f="%d"]'%j, e['ok'])
        pg.click('#hchk')
    return t
def run(pg, wrong_first):
    n=0; last=None; wrongs=0
    while True:
        rs=pg.evaluate('__dbg()')
        if rs is None: return n, wrongs, 'home'
        if rs['phase']=='study': pg.click('#gostart'); continue
        if rs['phase']=='summary': return n, wrongs, 'summary'
        w = wrong_first and rs['si']!=last; last=rs['si']
        t=solve(pg, w); wrongs += 1 if (w and ('(x)' in t or t=='gate')) else 0
        n+=1
        try: pg.wait_for_selector('#nx', timeout=4000)
        except Exception: pass
        time.sleep(0.7)

        if pg.locator('#nx').count(): pg.click('#nx')
        time.sleep(0.5)
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844})
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:%s/?test'%PORT); pg.fill('#nm','검수'); pg.click('#nameform button'); time.sleep(.5)
    for di in DAYS:
        if pg.locator('#quit').count(): pg.click('#quit'); time.sleep(.3)
        if not pg.locator('[data-go="%d"]'%di).count(): pg.locator('[data-sel="%d"]'%di).first.click()
        pg.locator('[data-go="%d"]'%di).first.click(); time.sleep(.3)
        # 단계마다 이어서 풀기: summary에서 다음 단계로
        tot=0; tw=0; guard=0
        while guard<40:
            guard+=1; n,w,ph=run(pg, True); tot+=n; tw+=w
            if ph!='summary': break
            if pg.locator('#toreview').count():
                pg.click('#toreview'); time.sleep(.5)
                rn,_,ph2=run(pg, False)
                print('   오답 학습', rn, '문제 풀고 →', ph2)
                if ph2=='summary' and pg.locator('#toreview').count(): print('   !! 오답 학습 뒤에도 오답이 남음'); 
                if ph2!='summary': break
            if pg.locator('#tonext').count(): pg.click('#tonext'); time.sleep(.3); continue
            break
        if pg.locator('#tores').count():
            pg.click('#tores'); time.sleep(.8)
            rb=pg.eval_on_selector_all('button,a','e=>e.filter(x=>x.offsetParent).map(x=>(x.id||"")+":"+x.innerText.replace(/\\s+/g," ").slice(0,30))')
            print('   결과 화면:', [x for x in rb if '오답' in x or '틀린' in x or '다시' in x][:5])
            cand=[x for x in rb if ('오답' in x or '틀린' in x) and x.split(':')[0]]
            if cand:
                pg.click('#'+cand[0].split(':')[0]); time.sleep(.6)
                rn,_,ph2=run(pg, False); print('   결과 화면 오답 다시 풀기', rn, '문제 →', ph2)
                if pg.locator('#tores').count(): pg.click('#tores'); time.sleep(.6)
                rb=pg.eval_on_selector_all('button,a','e=>e.filter(x=>x.offsetParent).map(x=>(x.id||"")+":"+x.innerText.replace(/\\s+/g," ").slice(0,30))')
                print('   다시 푼 뒤:', [x for x in rb if '오답' in x or '틀린' in x][:4])
        btns=pg.eval_on_selector_all('button','e=>e.filter(x=>x.offsetParent).map(x=>x.innerText.replace(/\\s+/g," ").slice(0,24))')
        print('DAY',di+1,'푼 문제',tot,'일부러 틀림',tw,'| 끝 화면 버튼:',btns[:4])
    # 오답 노트
    if pg.locator('#quit').count(): pg.click('#quit'); time.sleep(.3)
    pg.goto('http://localhost:%s/?test'%PORT); time.sleep(.8)
    nb=pg.locator('[data-note]').count(); print('오답 노트 묶음 버튼', nb)
    if nb:
        pg.locator('[data-note]').first.click(); time.sleep(.5)
        n,_,ph=run(pg, False); print('오답 노트', n, '문제 →', ph)
    b.close()
finally: srv.terminate()
print('errors:', errs or 'none')
