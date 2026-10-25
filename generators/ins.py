# 일치·불일치 단계를 교과서 단원 데이터에 넣는 도구
# Q[file] = { 'guide': ..., 'days': { 1: [ (box, stem, opts, per, ex), ... ], 2: [...] } }
# opts 첫 번째가 정답, per = [[선택지 해석, 근거(본문 일부 또는 목록 또는 ''), 판정], ...]
import json, sys, importlib.util
J = lambda x: json.dumps(x, ensure_ascii=False)
NOT = '글의 내용과 일치하지 <u>않는</u> 것은?'
YES = '글의 내용과 <u>일치하는</u> 것은?'

def insert(path, guide, days):
    s = open(path, encoding='utf-8').read()
    if "title: '일치·불일치'" in s:
        raise SystemExit(path + ': 이미 일치·불일치가 있음')
    parts = s.split("{ type: 'pick', title: '어법선택'")
    assert len(parts) == len(days) + 1, (path, len(parts) - 1, len(days))
    out = parts[0]
    for di in range(1, len(parts)):
        items = []
        for box, stem, opts, per, ex in days[di]:
            assert len(opts) == len(per) == 5, (path, di, opts[0])
            n = box[0] if len(box) == 1 else box[-1]
            items.append("        { n: %s, box: %s, q: %s, opts: %s, ex: %s, per: %s }" % (J(n), J(box), J(stem), J(opts), J(ex), J(per)))
        out += ("{ type: 'mc', title: '일치·불일치', guide: %s, items: [\n" % J(guide)) + ',\n'.join(items) + \
               "\n      ]},\n      { type: 'pick', title: '어법선택'" + parts[di]
    open(path, 'w', encoding='utf-8').write(out)
    print('ok', path)

if __name__ == '__main__':
    spec = importlib.util.spec_from_file_location('content', sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for path, (guide, days) in m.Q.items():
        insert('/home/claude/proj/data/' + path, guide, days)
