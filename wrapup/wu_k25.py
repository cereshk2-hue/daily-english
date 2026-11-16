# 11/16 학교 기출 원본 그대로(25문항 · 배점 제각각 · 정답 위치 원본 그대로) 빌더 — wu_nrt7.Test를 고쳐 씀
import inspect, re
import wu_nrt7 as B
from wu_nrt7 import *
src = inspect.getsource(B.Test.render)
src = src.replace("assert len(s.items) == 20, len(s.items)\n        s.place()", "pass")
src = src.replace("enumerate(ans[10:])) + '\\n  </div>", "enumerate(ans[10:20])) + '\\n    ' + ''.join('<div>%d<b>%s</b></div>' % (k + 21, a) for k, a in enumerate(ans[20:])) + '\\n  </div>")
src = src.replace('<div class="when">20문항 · 각 5점<br>제한 시간 30분</div>', '<div class="when">%d문항 · 100점<br>제한 시간 45분</div>')
src = src.replace("''' % (s.short, s.short, s.title, s.notice)", "''' % (s.short, s.short, s.title, len(s.items), s.notice)")
src = src.replace('<div class="when">각 5점 · 100점</div>', '<div class="when">배점은 문항 끝 [ ]</div>')
src = src.replace('<span>정답 분포 ①~⑤ 각 4개</span>', '<span>원본 정답 위치 그대로</span>')
src = src.replace('검수 후 오류 수정</span>', '원본 그대로</span>').replace('· 내신 대비</span>', '· 학교 기출</span>')
assert src.count('%d문항 · 100점') == 1 and 'k + 21' in src, '빌더 바뀜'
ns = {}; exec(compile('class _X:\n' + src, 'wu_k25', 'exec'), B.__dict__, ns)
class Test(B.Test):
    def fixed(s, stem, src_, body, opts, ans, ex, w, pts, en=True):
        B.Test.fixed(s, stem + ' <span class="pt">[%d점]</span>' % pts, src_, body, opts, ans, ex, w, en); s.items[-1]['pts'] = pts
Test.render = ns['_X'].render
