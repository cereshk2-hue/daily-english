# 11/24 범위 수정: 26번 제외, 모고 DAY 스크램블 삭제 (scope1124.py와 같은 결과)
# 11/18 대진고2 · 2026년 10월 고2 학평 20~24·26·29~42번 → h2-ne-oh-L3(능률 오선영 L3·4) 끝에 DAY로 붙임 (한 지문 = 하루, id q20…q41)
#  - 새로 쓴 지문: p20 p21 p22 p26 p29 p30 p32 p34 p35 p36 p38 p39 p40 (이 폴더)
#  - 안곡고2 때 만든 같은 지문 재사용: 23·24·31·33·37·41~42 = gen/angok2 p1~p6 (어휘만 해설서 WORDS로 교체, 라벨 '10월 ' 뺌)
import sys, json, subprocess, re, importlib
sys.path.insert(0, '/home/claude/work/gen'); sys.path.insert(0, '/home/claude/srcrepo/gen/dj2610'); sys.path.insert(1, '/home/claude/srcrepo/gen/angok2')
from gencommon import write
import jfw
REUSE = {'23': 'p1', '24': 'p2', '31': 'p3', '33': 'p4', '37': 'p5', '41~42': 'p6'}
MODS = [('20', '20 필자의 주장 · 정원사형 부모'), ('21', '21 밑줄 함축 의미 · 이자와 시간의 가치'), ('22', '22 글의 요지 · 콘텐츠 제작자의 책임'),
 ('23', '23 글의 주제 · 문어의 분산 신경계'), ('24', '24 글의 제목 · 아리스토텔레스 윤리학의 한계'),
 ('29', '29 어법 · 생존이라는 허들 경주'), ('30', '30 어휘 · 비언어 신호의 우위'), ('31', '31 빈칸 · 자동화된 기본 설정'),
 ('32', '32 빈칸 · 대중의 압박과 재판'), ('33', '33 빈칸 · 평생 이어지는 발달'), ('34', '34 빈칸 · 상호 연결과 실패의 확산'),
 ('35', '35 무관한 문장 · 전염병 치료의 진보'), ('36', '36 글의 순서 · 우리는 사용자가 아니다'), ('37', '37 글의 순서 · 감정 재평가'),
 ('38', '38 문장 삽입 · 용도에 따른 수질 기준'), ('39', '39 문장 삽입 · 결을 거슬러 읽는 사회사'), ('40', '40 요약문 · 돌고래의 병렬 처리'),
 ('41~42', '41~42 장문 · 지루함이라는 기회')]
def mod(n):
    if n in REUSE:
        m = importlib.import_module(REUSE[n])
        try: m.VOCAB = jfw.words(n)
        except Exception as e: print('words 실패', n, e)
        return m
    return importlib.import_module('p' + n)
def spread(d, n):
    return jfw.spread(d, re.match(r'\d+', str(n)).group())
def build():
    out = []
    for n, story in MODS:
        m = mod(n)
        d = spread(jfw.jday(n, 'DAY', '10월 모고 %s번' % n, story, m.p, m), n)
        d['id'] = 'q' + re.match(r'\d+', n).group()
        s = json.dumps(d, ensure_ascii=False).replace('10월 %s번' % n, '%s번' % n).replace('10월 모고 %s번' % n, '10월 모고 %s번' % n)
        d = json.loads(s); d['range'] = '10월 모고 %s번' % n
        d['steps'] = [st for st in d['steps'] if st['type'] != 'scramble']   # 11/24: 우리말→영작은 교과서 본문에서만
        out.append(d)
    return out
if __name__ == '__main__':
    path = '/home/claude/proj/data/h2-ne-oh-L3.js'
    PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('%s');process.stdout.write(JSON.stringify(window.PKG))" % path]))
    base = [d for d in PK['days'] if not re.match(r'q\d+$', d['id'])]
    PK['days'] = base + build()
    for i, d in enumerate(PK['days']): d['name'] = 'DAY %d' % (i + 1)
    PK['unit'] = '영어Ⅱ Lesson 3 · 4 + 10월 학평 20~24·29~42번'
    src = open(path, encoding='utf-8').read(); head = src[:src.index('window.PKG')]
    tail = src[src.index('/* WRAPUP-TESTS'):] if '/* WRAPUP-TESTS' in src else ''
    if '10월 고2 학평' not in head: head = head.rstrip('\n') + '\n/* 11/18: 2026년 10월 고2 학평(대진고 범위) 20~24·26·29~42번 DAY q20~q41 (한 지문 = 하루) gen/dj2610/mkattach.py — 해설서 hwp → extract*.py·prep.py, 23·24·31·33·37·41~42는 gen/angok2 재사용 */\n'
    PK.pop('tests', None)
    write(PK, path, head)
    if tail: open(path, 'a', encoding='utf-8').write(tail)
    print([(d['name'], d['range'], sum(len(s['items']) for s in d['steps'])) for d in PK['days'][len(base):]])
