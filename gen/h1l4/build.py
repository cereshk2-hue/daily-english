import json,common,d7,d8,d9
src=open('orig_L3.js').read()
days=[common.day('l4a','DAY 7','4과 본문 ❶❷','환경 위기 · 플라스틱 쓰레기와 밀웜',['❶','❷'],d7),
      common.day('l4b','DAY 8','4과 본문 ❸','버드나무로 오염된 흙 정화하기',['❸'],d8),
      common.day('l4c','DAY 9','4과 본문 ❹❺','커피 찌꺼기로 만드는 조류 바이오 연료 · 자연이 준 기회',['❹','❺'],d9)]
i=src.index('/* WRAPUP-TESTS'); head=src[:i]; tail=src[i:]
j=head.rindex('\n  ]'); 
assert head[j-4:j]==' ] }' or head[j-3:j]=='] }', head[j-20:j+5]
ins=''.join(',\n  '+json.dumps(d,ensure_ascii=False) for d in days)
head=head[:j]+ins+head[j:]
rep=[("unit: '공통영어2 Lesson 3',","unit: '공통영어2 Lesson 3 · 4',"),
     ("title: 'A Timeless Symbol of Korea',","title: 'A Timeless Symbol of Korea · Looking to Nature for Help',"),
     ("titleKo: '한국의 영원한 상징',","titleKo: '한국의 영원한 상징 · 자연에게 도움 구하기',"),
     ("/* 11/3: DAY 4~6","/* 11/5: DAY 7~9 = Lesson 4 (Toward Sustainability · Looking to Nature for Help) 본문 ❶~❺, work/l4/build.py */\n/* 11/3: DAY 4~6")]
for a,b in rep:
    assert a in head,a; head=head.replace(a,b,1)
open('/home/claude/proj/data/h1-ne-min-L3.js','w').write(head+tail)
for d in days: print(d['id'],d['name'],len(d['steps']),sum(len(s['items']) for s in d['steps']))
