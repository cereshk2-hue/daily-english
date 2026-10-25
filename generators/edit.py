# 고등 세트 난이도 올리기: 어휘선택 오답 교체, T/F 바꿔쓰기, 빈칸 오답 교체
import json, re, sys, importlib.util
J = lambda x: json.dumps(x, ensure_ascii=False)
EXQ = r"""('(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*")"""

def one(lines, pred, what):
    hit = [i for i, l in enumerate(lines) if pred(l)]
    assert len(hit) == 1, (what, len(hit))
    return hit[0]

def apply(path, P, T, B):
    lines = open(path, encoding='utf-8').read().split('\n')
    for old, new, ex in P:          # 어휘선택: {정답|오답} → {정답|새 오답}
        i = one(lines, lambda l: '{' + old + '}' in l and "s: " in l, old)
        l = lines[i].replace('{' + old + '}', '{' + new + '}')
        l, n = re.subn(r"ex: " + EXQ + r" \}", lambda m: 'ex: ' + J(ex) + ' }', l); assert n == 1, old
        lines[i] = l
    for old, new in T:               # T/F: 문장 시작으로 찾아 [새 문장, 참거짓, 해설, ...나머지] 로 바꿈
        i = one(lines, lambda l: l.lstrip().startswith('[') and re.search(r', (true|false), ', l) and (("['" + old) in l or ('["' + old) in l), old)
        ind = lines[i][:len(lines[i]) - len(lines[i].lstrip())]
        tail = ',' if lines[i].rstrip().endswith(',') else ''
        lines[i] = ind + '[' + ', '.join(J(x) for x in new) + ']' + tail
    for start, opts in B:            # 빈칸: 정답은 그대로, 오답 3개 교체
        i = one(lines, lambda l: (("s: '" + start) in l or ('s: "' + start) in l) and 'opts:' in l and '____' in l, start)
        m = re.search(r"opts: \[(.*?)\], ex:", lines[i]); assert m, start
        first = re.match(EXQ, m.group(1)).group(1)
        first_val = json.loads(first) if first.startswith('"') else first[1:-1].replace("\\'", "'")
        assert first_val == opts[0], (start, first_val, opts[0])
        lines[i] = lines[i][:m.start(1)] + ', '.join(J(o) for o in opts) + lines[i][m.end(1):]
    open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    print('ok', path, len(P), len(T), len(B))

if __name__ == '__main__':
    spec = importlib.util.spec_from_file_location('c', sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    apply('/home/claude/proj/data/' + m.FILE, m.P, m.T, m.B)
