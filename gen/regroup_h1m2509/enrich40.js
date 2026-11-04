const fs=require('fs');const P=require('./pkg.json');const d=P.days.find(d=>d.id==='p10');
const S=d.passage.filter(r=>r[0]!=='#').map(r=>r[1]);const K=d.passage.filter(r=>r[0]!=='#').map(r=>r[2]);
const step=t=>d.steps.find(s=>s.title===t);
const add=(t,arr)=>step(t).items.push(...arr);
add('어휘선택',[
 {s:"Vision is influenced by our {preconceptions|precautions} about reality.",ex:"정답 ▶ preconceptions (선입견)\n오답 ▶ precautions (예방 조치)\n이유: 망치를 '쓸 준비된' 각도로 떠올리듯, 우리의 시각은 현실에 대한 '선입견'에 영향을 받아요."},
 {s:"In viewing a scene, we establish unconscious hierarchies that reflect our functional relationship to objects and our {momentary|monetary} priorities.",ex:"정답 ▶ momentary (순간적인, 그 순간의)\n오답 ▶ monetary (금전적인)\n이유: 장면을 볼 때 '그 순간'의 우선순위가 반영돼요. 철자가 비슷하니 주의!"},
 {s:"For example, when visualizing a hammer in our mind's eye, we tend to \"see\" it in {profile|proportion} or at some other \"ready for use\" angle.",ex:"정답 ▶ profile (in profile 옆모습으로)\n오답 ▶ proportion (비율)\n이유: 망치를 '옆모습'이나 바로 쓸 수 있는 각도로 떠올린다는 뜻이에요."},
 {s:"The functional relationship we have with objects creates visual {expectations|explanations} that interfere with our ability to see \"like a camera.\"",ex:"정답 ▶ expectations (기대)\n오답 ▶ explanations (설명)\n이유: 사물을 쓰는 방식 때문에 '이렇게 보일 것'이라는 시각적 기대가 생기고, 그 기대가 카메라처럼 보는 것을 방해해요."},
 {s:"When we look at them carefully, photographs are often surprising because they don't interpret confusing details but simply serve them up to us with a mechanical {indifference|interference}.",ex:"정답 ▶ indifference (무관심)\n오답 ▶ interference (간섭, 방해)\n이유: 사진은 세부를 해석하지 않고 '기계적인 무관심'으로 그냥 내놓아요. = impartially(치우침 없이)"}
]);
add('T/F 내용 확인',[
 ["Our momentary priorities have no effect on how we view a scene.",false,"정답 ▶ F\n이유: 장면을 볼 때 세우는 위계는 그 순간의 우선순위를 반영해요(reflect).\n어휘 ▶ have no effect on ~에 영향이 없다",40,"our momentary priorities"],
 ["Most people would imagine a hammer seen from the top with its handle hidden.",false,"정답 ▶ F\n이유: 위에서 본 망치(손잡이가 가려진 모습)는 아마 떠올리지 않는다고 했어요.",40,"One would probably not visualize a hammer as seen from the top"],
 ["The way we use objects makes it harder for us to see like a camera.",true,"정답 ▶ T\n이유: 사물과의 기능적 관계가 '카메라처럼' 보는 능력을 방해해요.\n어휘 ▶ the way we use objects = our functional relationship to objects",40,"interfere with our ability to see"],
 ["A camera records the world without taking sides.",true,"정답 ▶ T\n이유: 카메라는 세상을 치우침 없이(impartially) 기록해요.\n어휘 ▶ take sides 한쪽 편을 들다",40,"documents the world impartially"],
 ["Photographs surprise us because they add extra details to a scene.",false,"정답 ▶ F\n이유: 세부를 더하는 게 아니라, 해석하지 않고 그대로 내놓기 때문에 놀라워요.",40,"simply serve them up to us"],
 ["The hierarchies we set up when viewing a scene are conscious and deliberate.",false,"정답 ▶ F\n이유: 우리가 세우는 위계는 '무의식적인(unconscious)' 것이에요.\n어휘 ▶ deliberate 의도적인",40,"unconscious hierarchies"]
]);
add('어법선택',[
 {s:"In viewing a scene, we establish unconscious hierarchies that {reflect|reflects} our functional relationship to objects and our momentary priorities.",ex:"정답 ▶ reflect\n이유: 주격 관계대명사 that의 선행사는 hierarchies(복수) → reflect"},
 {s:"For example, when {visualizing|visualized} a hammer in our mind's eye, we tend to \"see\" it in profile or at some other \"ready for use\" angle.",ex:"정답 ▶ visualizing\n이유: 접속사를 남긴 분사구문. 우리가 망치를 '떠올리는' 능동 → when (we are) visualizing"},
 {s:"The functional relationship we have with objects {creates|create} visual expectations that interfere with our ability to see \"like a camera.\"",ex:"정답 ▶ creates\n이유: 주어는 The functional relationship(단수). we have with objects는 목적격 관계대명사가 생략된 수식어"},
 {s:"It documents the world impartially through a lens {that|what} is similar to the eye.",ex:"정답 ▶ that\n이유: 앞에 선행사 a lens가 있음 → 관계대명사 that. what은 선행사를 품고 있어 앞에 명사가 오면 못 써요."},
 {s:"When we look at them carefully, photographs are often surprising because they don't interpret confusing details but simply {serve|serving} them up to us with a mechanical indifference.",ex:"정답 ▶ serve\n이유: don't interpret ~ but (simply) serve ~ : not A but B 병렬. 둘 다 동사원형"},
 {s:"And because of their flatness, photographs often contain areas that {appear|appears} as unrecognizable colors and shapes.",ex:"정답 ▶ appear\n이유: 주격 관계대명사 that의 선행사는 areas(복수) → appear"}
]);
add('동사변형',[
 {s:"Vision is ___ by our preconceptions about reality.",v:"influence",a:["influenced"],ex:"정답 ▶ influenced\n이유: 시각이 선입견에 '영향을 받는' 수동 → be + p.p. + by"},
 {s:"For example, when ___ a hammer in our mind's eye, we tend to \"see\" it in profile or at some other \"ready for use\" angle.",v:"visualize",a:["visualizing"],ex:"정답 ▶ visualizing\n이유: 접속사 when을 남긴 분사구문, 우리가 '떠올리는' 능동 → 현재분사"},
 {s:"The functional relationship we have with objects creates visual expectations that ___ with our ability to see \"like a camera.\"",v:"interfere",a:["interfere"],ex:"정답 ▶ interfere\n이유: that의 선행사는 expectations(복수) → interfere (현재시제, 3인칭 복수)"},
 {s:"And because of their flatness, photographs often contain areas that ___ as unrecognizable colors and shapes.",v:"appear",a:["appear"],ex:"정답 ▶ appear\n이유: that의 선행사는 areas(복수) → appear"}
]);
add('오류찾기',[
 {s:"In [[viewing]] a scene, we establish unconscious hierarchies that [[reflects]] our functional relationship to objects and our [[momentary]] priorities.",w:1,fix:"reflect",ex:"틀린 곳 ▶ ② reflects → reflect\n이유: 선행사 hierarchies(복수)\n나머지 ▶ ① 전치사 In + 동명사 ✔ ③ momentary(그 순간의) ✔"},
 {s:"One would probably not visualize a hammer as [[seeing]] from the top so that the handle [[is]] [[hidden]] by the hammer's head.",w:0,fix:"seen",ex:"틀린 곳 ▶ ① seeing → seen\n이유: 망치가 위에서 '보이는' 수동 → as (it is) seen\n나머지 ▶ ② is ③ hidden: 손잡이가 '가려지는' 수동 ✔"},
 {s:"The functional relationship we have with objects [[create]] visual expectations that [[interfere]] with our ability [[to see]] \"like a camera.\"",w:0,fix:"creates",ex:"틀린 곳 ▶ ① create → creates\n이유: 주어는 The functional relationship(단수)\n나머지 ▶ ② 선행사 expectations(복수) ✔ ③ ability to see(~할 능력) ✔"},
 {s:"And [[because]] their flatness, photographs often [[contain]] areas that [[appear]] as unrecognizable colors and shapes.",w:0,fix:"because of",ex:"틀린 곳 ▶ ① because → because of\n이유: 뒤에 명사구(their flatness)만 있음 → 전치사\n나머지 ▶ ② 주어 photographs ✔ ③ 선행사 areas ✔"}
]);
add('본문 스크램블',[2,7,8,3].map(i=>({ko:K[i].replace(/^카메라는 눈과/,'카메라는 눈과'),en:S[i]})));
add('문장순서',[{lines:S.slice(0,4),flow:["시각은 선입견의 영향을 받음","장면을 볼 때 무의식적 위계를 세움","예: 망치는 '쓸 준비된' 각도로 떠올림","위에서 본 망치는 떠올리지 않음"]}]);
add('문장삽입',[{lines:S.slice(1,5),given:2,flow:["장면을 볼 때 무의식적 위계를 세움","예: 망치는 옆모습 등 '쓸 준비된' 각도로","위에서 본(손잡이가 가려진) 망치는 떠올리지 않음","기능적 관계 → '카메라처럼' 보기 방해"],ex:"정답 ▶ ②\n이유: '옆모습이나 쓸 준비된 각도로 본다'는 예시 바로 뒤에 '위에서 본 모습으로는 떠올리지 않는다'가 이어져야 해요. 두 문장 모두 a hammer를 이야기해요."}]);
add('어색한 문장',[{lines:[S[5],S[6],"Therefore, a camera focuses only on the objects that matter most to the photographer.",S[7]],odd:2,ex:"정답 ▶ ③\n이유: 카메라는 치우침 없이(impartially), 기계적인 무관심으로 기록해요. 사진가에게 중요한 것만 골라 찍는다는 내용은 흐름과 반대예요."}]);
add('빈칸추론',[
 {s:"The functional relationship we have with objects creates visual ____ that interfere with our ability to see \"like a camera.\"",opts:["expectations","instructions","exceptions","experiments"],ex:"정답 ▶ expectations (기대)\n이유: 사물을 쓰는 방식 때문에 '이렇게 보일 것'이라는 기대가 생겨 카메라처럼 보지 못해요.\n오답 ▶ instructions 지시 · exceptions 예외 · experiments 실험"},
 {s:"When we look at them carefully, photographs are often surprising because they don't interpret confusing details but simply serve them up to us with a mechanical ____.",opts:["indifference","enthusiasm","sympathy","creativity"],ex:"정답 ▶ indifference (무관심)\n이유: 카메라는 해석 없이 '기계적으로' 내놓아요 → 감정·해석이 없는 무관심.\n오답 ▶ enthusiasm 열정 · sympathy 공감 · creativity 창의성"},
 {s:"And because of their ____, photographs often contain areas that appear as unrecognizable colors and shapes.",opts:["flatness","brightness","sharpness","thickness"],ex:"정답 ▶ flatness (평면성)\n이유: 사진은 입체가 아닌 평면이라 알아볼 수 없는 색과 형태로 보이는 부분이 생겨요."}
]);
const gram=[
 {q:"빈칸에 알맞은 것은?<br><b>Vision is influenced ______ our preconceptions about reality.</b>",opts:["by","with","at","for"],ex:"정답 ▶ by\n이유: 수동태 be + p.p. + by(행위자)\n본문 ▶ Vision is influenced by our preconceptions"},
 {q:"빈칸에 알맞은 것은?<br><b>When ______ a hammer in our mind's eye, we tend to see it in profile.</b>",opts:["visualizing","visualized","visualize","to visualize"],ex:"정답 ▶ visualizing\n이유: 접속사를 남긴 분사구문. 주어 we가 '떠올리는' 능동 → 현재분사\n본문 ▶ when visualizing a hammer in our mind's eye"},
 {q:"빈칸에 알맞은 것은?<br><b>The relationship ______ we have with objects creates visual expectations.</b>",opts:["that","what","whose","where"],ex:"정답 ▶ that\n이유: have의 목적어 역할 → 목적격 관계대명사 that(생략 가능)\n오답 ▶ what은 선행사가 없을 때, whose는 뒤에 명사, where는 뒤에 완전한 문장\n본문 ▶ The functional relationship we have with objects (that 생략)"},
 {q:"어법상 알맞은 것은?<br><b>The camera, like the human eye, ______ only shapes and colors.</b>",opts:["sees","see","seeing","to see"],ex:"정답 ▶ sees\n이유: 주어는 The camera(단수). 콤마 사이 like the human eye는 삽입구라 수일치와 상관없어요."},
 {q:"빈칸에 알맞은 것은?<br><b>Photographs don't interpret details ______ simply serve them up to us.</b>",opts:["but","or","so","nor"],ex:"정답 ▶ but\n이유: not A but B (A가 아니라 B)\n본문 ▶ they don't interpret confusing details but simply serve them up"},
 {q:"빈칸에 알맞은 것은?<br><b>______ their flatness, photographs often contain unrecognizable areas.</b>",opts:["Because of","Because","Although","Unless"],ex:"정답 ▶ Because of\n이유: 뒤에 명사구(their flatness)만 있음 → 전치사 because of. Because·Although·Unless는 접속사라 뒤에 주어+동사가 와야 해요."}
];
let gs=step('핵심문법');
if(!gs){const p6=P.days.find(x=>x.id==='p6');gs=Object.assign({},p6.steps.find(s=>s.title==='핵심문법'),{items:[]});d.steps.splice(d.steps.findIndex(s=>s.title==='요약문 완성'),0,gs);}
gs.items.push(...gram);
// story fixes
P.days.find(x=>x.id==='p8').story='36 · 37 글의 순서';P.days.find(x=>x.id==='p9').story='38 · 39 문장 삽입';
fs.writeFileSync('pkg.json',JSON.stringify(P));
P.days.slice(5).forEach(x=>console.log(x.id,x.story,x.steps.length,x.steps.reduce((n,s)=>n+s.items.length,0)));
console.log(K[2],'|',K[7],'|',K[8],'|',K[3]);
