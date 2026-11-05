import json,common,y1,y2,y3
J=lambda x: json.dumps(x,ensure_ascii=False)
def sq(s): return "'"+s.replace('\\','\\\\').replace("'","\\'")+"'"
days=[common.day('y1','DAY 1','3과 본문 ❶❷','수학 영재 캐서린 · 차별 속에서 이어 간 공부',['❶','❷'],y1),
      common.day('y2','DAY 2','3과 본문 ❸','NASA의 흑인 컴퓨터 · 차별에 맞선 질문',['❸'],y2),
      common.day('y3','DAY 3','3과 본문 ❹❺','손 계산으로 연 우주 시대 · 은퇴 후의 공헌과 유산',['❹','❺'],y3)]
out=["/* 고1 공통영어2 YBM(김은형) Lesson 3 · Beyond Barriers (본문: Katherine Johnson, a \"Computer\" Who Looked Beyond Numbers)",
     "   중산고 1학년 2학기 기말 · 본문은 이그잼포유 hwp 문장 학습에서 추출. work/ybm3/gen/build.py 로 만듦 */",
     "window.PKG = {","  id: 'h1-ybm-kim-L3',","  school: '고1 YBM(김은형)',","  unit: '공통영어2 Lesson 3',",
     "  title: "+sq('Katherine Johnson, a "Computer" Who Looked Beyond Numbers')+",","  titleKo: "+sq("숫자 너머를 본 '컴퓨터' 캐서린 존슨")+",",
     "  exam: '2학기 기말고사',","  prose: true,","  teacherPhone: '',","  days: ["]
for k,d in enumerate(days):
    out.append("  { id: %s, name: %s, range: %s, story: %s, passage: %s, steps: ["%(sq(d['id']),sq(d['name']),sq(d['range']),sq(d['story']),J(d['passage'])))
    for i,s in enumerate(d['steps']):
        rest={k2:v for k2,v in s.items() if k2!='type'}
        out.append("    { type: %s, %s }%s"%(sq(s['type']),J(rest)[1:-1],',' if i<len(d['steps'])-1 else ''))
    out.append("  ] }"+(',' if k<len(days)-1 else ''))
out.append("  ]"); out.append("};")
open('/home/claude/proj/data/h1-ybm-kim-L3.js','w').write('\n'.join(out)+'\n')
for d in days: print(d['id'],sum(len(s['items']) for s in d['steps']))
