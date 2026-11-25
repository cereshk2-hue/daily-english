# 11/25 안곡고2 비밀노트 변형문제: 2026 9월 고2 학평 24·29·30·34·38·41(~42)번
# 중산고2 비밀노트(jsb-*, wrapup/bimi3 · 같은 시험 같은 edu-lab 파일)에서 해당 번호 문항만 그대로 가져옴
# 번호 = 원본 시험지 번호(중산고2와 같음, 서술형 없음). 끝 AGB-TESTS 블록(여러 번 돌려도 같음)
import json, re, subprocess
SRC = '/home/claude/proj/data/h2-mock-2609-jungsan.js'
DST = '/home/claude/proj/data/h2-mock-2609-angok.js'
T = {t['id']: t for t in json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG.tests))" % SRC])) if t.get('kind') == 'bimi'}
PLAN = [('agb-24', 'jsb-2426', ['24번'], '24번'), ('agb-2930', 'jsb-2930', ['29번', '30번'], '29·30번'),
        ('agb-34', 'jsb-3334', ['34번'], '34번'), ('agb-38', 'jsb-3738', ['38번'], '38번'), ('agb-4142', 'jsb-4142', ['41·42번'], '41·42번')]
out = []
for nid, sid, srcs, lab in PLAN:
    its = [dict(i) for i in T[sid]['items'] if i['src'] in srcs]
    # 같은 지문 묶음(grp)은 첫 문항(지문 들어 있는 문항)이 꼭 들어 있어야 함
    for g in {i.get('grp') for i in its if i.get('grp') not in (None, 0)}:
        first = [i for i in T[sid]['items'] if i.get('grp') == g][0]
        assert first['src'] in srcs, (nid, g)
    t = {'id': nid, 'kind': 'bimi', 'title': '비밀노트 변형문제 ' + lab, 'short': '비밀노트 ' + lab, 'school': '안곡고 2학년',
         'minutes': max(20, min(50, 5 * round(len(its) * 2.2 / 5))), 'items': its}
    out.append(t); print(nid, len(its), '문항 · 번호', its[0]['n'], '~', its[-1]['n'], '· 정답', ''.join('①②③④⑤'[a] if isinstance(a, int) else '[' + ''.join('①②③④⑤'[x] for x in a) + ']' for a in (i['ans'] for i in its)))
ids = [t['id'] for t in out]
blk = ('/* AGB-TESTS: 11/25 안곡고2 비밀노트 변형문제 (gen/ag2609/add_bimi.py — 중산고2 jsb-*에서 해당 번호만 · 손으로 고치지 말 것) */\n'
       'window.PKG.tests=(window.PKG.tests||[]).filter(function(t){return %s.indexOf(t.id)<0}).concat(%s);\n/* /AGB-TESTS */\n') % (json.dumps(ids), json.dumps(out, ensure_ascii=False))
s = open(DST, encoding='utf-8').read()
s = re.sub(r'/\* AGB-TESTS:.*?/\* /AGB-TESTS \*/\n', '', s, flags=re.S)
open(DST, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n' + blk)
