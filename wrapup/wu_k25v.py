# 11/20 중산중 2025 기출 변형(25문항 · 배점 문항별 · 45분) 빌더 — wu_jsg 방식(정답 ①~⑤ 각 5개 자동 배치) + wu_k25 정답표(21~25번 줄)
import inspect, re
import wu_nrt7 as B
from wu_nrt7 import *
NQ = 25
src = inspect.getsource(B.Test.render)
src = src.replace("assert len(s.items) == 20, len(s.items)", "assert len(s.items) == NQ, len(s.items)")
src = src.replace("enumerate(ans[10:])) + '\\n  </div>", "enumerate(ans[10:20])) + '\\n    ' + ''.join('<div>%d<b>%s</b></div>' % (k + 21, a) for k, a in enumerate(ans[20:])) + '\\n  </div>")
src = src.replace('<div class="when">20문항 · 각 5점<br>제한 시간 30분</div>', '<div class="when">%d문항 · 100점<br>제한 시간 45분</div>')
src = src.replace("''' % (s.short, s.short, s.title, s.notice)", "''' % (s.short, s.short, s.title, len(s.items), s.notice)")
src = src.replace('<div class="when">각 5점 · 100점</div>', '<div class="when">배점은 문항 끝 [ ]</div>')
src = src.replace('<span>정답 분포 ①~⑤ 각 4개</span>', '<span>정답 분포 ①~⑤ 각 5개</span>')
src = src.replace('· 내신 대비</span>', '· 기출 변형</span>')
assert src.count('%d문항 · 100점') == 1 and 'k + 21' in src and 'NQ' in src, '빌더 바뀜'
psrc = inspect.getsource(B.Test.place).replace("assert cnt == [4] * 5, cnt", "assert cnt == [5] * 5, cnt").replace("assert max(cnt) <= 4,", "assert max(cnt) <= 5,")
assert '[5] * 5' in psrc
ns = {}; exec(compile('class _X:\n' + src + psrc, 'wu_k25v', 'exec'), dict(B.__dict__, NQ=NQ), ns)
PT = lambda p: ' <span class="pt">[%d점]</span>' % p
class Test(B.Test):
    def flex(s, stem, src_, body, opts, ex, w, pts, en=True):
        B.Test.flex(s, stem + PT(pts), src_, body, opts, ex, w, en); s.items[-1]['pts'] = pts
    def fixed(s, stem, src_, body, opts, ans, ex, w, pts, en=True):
        B.Test.fixed(s, stem + PT(pts), src_, body, opts, ans, ex, w, en); s.items[-1]['pts'] = pts
Test.render = ns['_X'].render
Test.place = ns['_X'].place
