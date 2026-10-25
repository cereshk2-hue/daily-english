import json

def P(n, rows):
    return [['', n, '']] + [['', e, k] for e, k in rows]

e = lambda S, i: S[i][0]

GV = '알맞은 답을 고르세요.'
MCG = "선택지는 본문을 어려운 어휘로 바꿔 쓴 문장이에요. 풀고 나서 해설의 어휘를 꼭 확인하세요."

def steps(vocab, pickv, tf, ilchi, pickg, verb, error, scr, order, insert, odd, blank, gram):
    return [
     {'type': 'vocab', 'title': '핵심어휘·숙어', 'quizN': 15, 'items': vocab},
     {'type': 'pick', 'title': '어휘선택', 'guide': '문맥에 맞는 낱말을 고르세요.', 'items': [{'s': s, 'ex': x} for s, x in pickv]},
     {'type': 'tf', 'title': 'T/F 내용 확인', 'guide': '본문 내용과 일치하면 T, 다르면 F를 고르세요.', 'items': tf},
     {'type': 'mc', 'title': '일치·불일치', 'guide': MCG, 'items': ilchi},
     {'type': 'pick', 'title': '어법선택', 'guide': '어법상 알맞은 것을 고르세요.', 'items': [{'s': s, 'ex': x} for s, x in pickg]},
     {'type': 'verb', 'title': '동사변형', 'guide': '( ) 안의 동사를 알맞은 형태로 바꿔 쓰세요.', 'items': [{'s': s, 'v': v, 'a': a, 'ex': x} for s, v, a, x in verb]},
     {'type': 'error', 'title': '오류찾기', 'guide': '어법상 틀린 곳을 고르세요.', 'items': [{'s': s, 'w': w, 'fix': f, 'ex': x} for s, w, f, x in error]},
     {'type': 'scramble', 'title': '본문 스크램블', 'guide': '우리말에 맞게 단어를 눌러 문장을 완성하세요.', 'items': [{'ko': k, 'en': en} for en, k in scr]},
     {'type': 'order', 'title': '문장순서', 'guide': '문장을 본문 순서대로 눌러서 배열하세요.', 'items': [{'lines': l, 'flow': f} for l, f in order]},
     {'type': 'insert', 'title': '문장삽입', 'guide': '주어진 문장이 들어가기에 가장 알맞은 곳을 고르세요.', 'items': [{'lines': l, 'given': g, 'flow': f, 'ex': x} for l, g, f, x in insert]},
     {'type': 'odd', 'title': '어색한 문장', 'guide': '글의 흐름과 관계없는 문장을 고르세요.', 'items': [{'lines': l, 'odd': o, 'ex': x} for l, o, x in odd]},
     {'type': 'blank', 'title': '빈칸추론', 'guide': '빈칸에 들어갈 말로 가장 알맞은 것을 고르세요.', 'items': [{'s': s, 'opts': o, 'ex': x} for s, o, x in blank]},
     {'type': 'mc', 'title': '핵심문법', 'guide': GV, 'items': [{'q': q, 'opts': o, 'ex': x} for q, o, x in gram]},
    ]

B = '빈칸에 알맞은 것은?<br><b>'

def js(v, ind=''):
    if isinstance(v, bool): return 'true' if v else 'false'
    if isinstance(v, (int, float)): return str(v)
    if isinstance(v, str): return "'" + v.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n') + "'"
    if isinstance(v, list):
        if v and isinstance(v[0], dict): return '[\n' + ',\n'.join(ind + '  ' + js(x, ind + '  ') for x in v) + '\n' + ind + ']'
        return '[' + ', '.join(js(x, ind) for x in v) + ']'
    return '{ ' + ', '.join(k + ': ' + js(x, ind) for k, x in v.items()) + ' }'

def write(PKG, path, header):
    body = ',\n'.join("  %s: %s" % (k, js(v)) for k, v in PKG.items() if k != 'days')
    days = ',\n'.join('  ' + js(d, '  ') for d in PKG['days'])
    open(path, 'w').write(header + "window.PKG = {\n" + body + ",\n  days: [\n" + days + "\n  ]\n};\n")
