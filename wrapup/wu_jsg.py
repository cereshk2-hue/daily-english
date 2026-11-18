# 11/18 중산중 기출 선별(17문항 · 배점 문항별) 빌더 — wu_nrt7.Test를 고쳐 씀
# 정답 위치는 고르게(①~⑤ 3~4개씩) 자동 배치(flex·table), 원본 위치가 필요한 것(ⓐ~ⓔ·삽입 위치)은 fixed
import inspect, re
import wu_nrt7 as B
from wu_nrt7 import *
NQ = 17
src = inspect.getsource(B.Test.render)
src = src.replace("assert len(s.items) == 20, len(s.items)", "assert len(s.items) == NQ, len(s.items)")
src = src.replace('<div class="when">20문항 · 각 5점<br>제한 시간 30분</div>', '<div class="when">%d문항 · 100점<br>제한 시간 35분</div>')
src = src.replace("''' % (s.short, s.short, s.title, s.notice)", "''' % (s.short, s.short, s.title, len(s.items), s.notice)")
src = src.replace('<div class="when">각 5점 · 100점</div>', '<div class="when">배점은 문항 끝 [ ]</div>')
src = src.replace('<span>정답 분포 ①~⑤ 각 4개</span>', '<span>정답 분포 ①~⑤ 고르게</span>')
src = src.replace('· 내신 대비</span>', '· 학교 기출</span>')
assert src.count('%d문항 · 100점') == 1 and 'NQ' in src, '빌더 바뀜'
psrc = inspect.getsource(B.Test.place).replace("assert cnt == [4] * 5, cnt", "assert max(cnt) - min(cnt) <= 1, cnt")
assert 'max(cnt) - min(cnt)' in psrc
ns = {}; exec(compile('class _X:\n' + src + psrc, 'wu_jsg', 'exec'), dict(B.__dict__, NQ=NQ), ns)
PT = lambda p: ' <span class="pt">[%d점]</span>' % p
class Test(B.Test):
    def flex(s, stem, src_, body, opts, ex, w, pts, en=True):
        B.Test.flex(s, stem + PT(pts), src_, body, opts, ex, w, en); s.items[-1]['pts'] = pts
    def table(s, stem, src_, body, cols, rows, ex, w, pts, ko=None):
        B.Test.table(s, stem + PT(pts), src_, body, cols, rows, ex, w, ko); s.items[-1]['pts'] = pts
    def fixed(s, stem, src_, body, opts, ans, ex, w, pts, en=True):
        B.Test.fixed(s, stem + PT(pts), src_, body, opts, ans, ex, w, en); s.items[-1]['pts'] = pts
    def pts(s):
        p = [it['pts'] for it in s.items]; assert sum(p) == 100, sum(p); return p
Test.render = ns['_X'].render
Test.place = ns['_X'].place
