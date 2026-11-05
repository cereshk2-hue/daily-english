# 11/5 밤: 안곡고 고2 모의고사 단원 뒤에 '영어Ⅱ 수능유형문제 연습'(10월 모평 6문항 · 고3 6월 모평 4문항)을 한 문제 = 하루로 DAY 5~14 추가
import json,fw,importlib
src=open('orig_angok.js').read()
DAYS=[('p1','10월 23번','문어 팔의 뉴런과 빨판'),('p2','10월 24번','아리스토텔레스 윤리학의 한계'),('p3','10월 31번','습관(자동화)은 결함이 아니다'),
 ('p4','10월 33번','가소성: 평생 이어지는 발달'),('p5','10월 37번','재평가: 감정을 근본에서 바꾸기'),('p6','10월 41~42번','지루함은 성장의 기회'),
 ('p7','고3 6월 24번','필수품을 넘어선 음식 문화'),('p8','고3 6월 35번','빠르게 녹는 빙하'),('p9','고3 6월 40번','기술적 실업의 이중 위협'),('p10','고3 6월 41~42번','일상에 녹아드는 기술')]
days=[]
for k,(mod,rng,story) in enumerate(DAYS):
    m=importlib.import_module(mod); days.append(fw.day('e%d'%(k+1),'DAY %d'%(k+5),rng,story,m.p,m))
end=src.rindex('\n  ]\n};'); assert src[end-5:end]==']  ] }'[-5:] or True
src=src[:end]+''.join(',\n  '+json.dumps(d,ensure_ascii=False) for d in days)+src[end:]
a="unit: '24·29·30·34·38·40·41~42번',"; assert a in src
src=src.replace(a,"unit: '24·29·30·34·38·40·41~42번 + 10월 · 고3 6월 모평',",1)
src=src.replace('*/','\n   DAY 5~14 = 영어Ⅱ 수능유형문제 연습(10월 모평 23·24·31·33·37·41~42 / 고3 6월 모평 24·35·40·41~42), 한 문제 = 하루. work/angok/gen/attach.py\n*/',1)
open('/home/claude/proj/data/h2-mock-2609-angok.js','w').write(src)
for d in days: print(d['id'],d['name'],d['range'],sum(len(s['items']) for s in d['steps']))
