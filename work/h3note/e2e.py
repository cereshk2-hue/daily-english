import subprocess, time, sys, json
from playwright.sync_api import sync_playwright
srv=subprocess.Popen([sys.executable,'-m','http.server','8771','-d','dist/github/h3-suneung-2510-kb7so'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
errs=[]; DAY0=1793664000000  # 2026-11-03 09:00 KST
def solve(pg,wrong=False):
    rs=pg.evaluate('__dbg()'); q=rs['qs'][rs['qi']]; t=q['t']
    if t in('choice','pick'):
        i=q['opts'].index(q['ans']); i=(i+1)%len(q['opts']) if wrong else i
        pg.locator('.opt').nth(i).click()
    elif t=='verb': pg.fill('#vin', 'zzz' if wrong else q['a'][0]); pg.click('#vf button')
    return q
def notes(pg): 
    S=pg.evaluate("JSON.parse(localStorage.getItem('daily:h3-suneung-2510:테스트'))"); return S.get('note',{})
def run(pg,wrongset):
    """현재 RS를 끝까지 풂. wrongset: 틀릴 (단계제목 일부) 집합, 단계마다 첫 문제만 틀림"""
    done=set()
    while True:
        rs=pg.evaluate('__dbg()')
        if rs is None: return
        if rs['phase']=='study': pg.click('#gostart'); continue
        if rs['phase']=='summary': return
        q=rs['qs'][rs['qi']]; st=q.get('stepTitle') or ''
        title=pg.evaluate("(function(){var r=__dbg();return (window.PKG.days[r.di].steps[r.si]||{}).title||''})()")
        w = any(k in title for k in wrongset) and title not in done and not rs.get('practice')
        solve(pg,w); 
        if w: done.add(title); print('  틀림:',title, '| notebar:', pg.locator('.notebar').inner_text() if pg.locator('.notebar').count() else '(없음)')
        pg.click('#nx')
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':390,'height':844})
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    def at(day):
        pg.clock.set_fixed_time(DAY0+day*86400000)
    at(0); pg.goto('http://localhost:8771/?test'); pg.fill('#nm','테스트'); pg.click('#nameform button')
    # DAY 1: 실전 틀리고 단어 리스트·단어 테스트 첫 문제 틀림
    pg.locator('[data-go="0"]').first.click()
    # 실전은 단계별 시작
    for k in range(3):
        if pg.evaluate('__dbg()') is None:
            if pg.locator('#tonext').count(): pg.click('#tonext')
        run(pg,{'실전','단어 리스트','단어 테스트'})
        if pg.locator('#tonext').count(): pg.click('#tonext')
        elif pg.locator('#tores').count(): pg.click('#tores'); break
    N=notes(pg); print('노트:',[ (e['q'].get('stepTitle'),e['q'].get('key')) for e in N.values()])
    # 다음 날 3일 동안: 홈에서 오늘의 오답 -> 매일 다 맞힘
    for d in (1,2,3):
        at(d); pg.goto('http://localhost:8771/?test'); time.sleep(.5)
        if pg.locator('#quit').count(): pg.click('#quit')
        pg.screenshot(path='/home/claude/work/h3note/home%d.png'%d,full_page=True)
        #print('   buttons:', pg.eval_on_selector_all('[data-go],[data-sel],[data-note]','e=>e.map(x=>x.outerHTML.slice(0,80))')[:8])
        pg.locator('[data-sel="1"]').first.click(); time.sleep(.2); pg.locator('[data-go="1"]').first.click(); time.sleep(.3)
        gate=pg.locator('#gnote').count(); print('day+%d 게이트:'%d, pg.locator('h2').first.inner_text() if gate else '없음')
        if gate:
            pg.click('#gnote'); run(pg,set())
        N=notes(pg); print('   노트 상태:',[(e['q'].get('key'),e.get('hit'),e.get('ok')) for e in N.values()])
    b.close()
finally: srv.terminate()
print('errors:',errs or 'none')
