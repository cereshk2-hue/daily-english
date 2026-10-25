# python3 tools/build.py
#  → dist/github/            GitHub Pages에 올릴 전체 (선생님 보드 index.html + 단원 폴더들 + 앱 설치 파일)
#  → dist/preview-<폴더>.html 단원별 한 파일 미리보기
import re, os, shutil, glob, json, secrets, string
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=open(os.path.join(R,'index.html'),encoding='utf-8').read()
gh=os.path.join(R,'dist','github'); shutil.rmtree(gh,ignore_errors=True); os.makedirs(gh)
# 추측할 수 없는 주소: 한 번 정한 코드는 tools/secrets.json에 저장해 링크가 바뀌지 않게 한다
SP=os.path.join(R,'tools','secrets.json'); SEC=json.load(open(SP)) if os.path.exists(SP) else {'units':{}}
code=lambda n: ''.join(secrets.choice(string.ascii_lowercase+string.digits) for _ in range(n))
SEC.setdefault('board','t-'+code(8))
def wrap(page):
    he=page.index('</style>')+len('</style>')
    return '<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'+page[:he]+'\n</head>\n<body>'+page[he:]+'</body>\n</html>\n'
units=[]
for f in sorted(glob.glob(os.path.join(R,'data','*.js'))):
    did=os.path.basename(f)[:-3]; js=open(f,encoding='utf-8').read()
    get=lambda k: re.search(k+r":\s*'([^']*)'",js).group(1)
    title,school,unit=get('title'),get('school'),get('unit')
    base=did.replace('-so-','-'); SEC['units'].setdefault(base,code(5)); folder=base+'-'+SEC['units'][base]
    grade,publisher=school.split(' ',1)
    days=[{'name':m[0],'range':m[1]} for m in re.findall(r"name:\s*'([^']+)',\s*range:\s*'([^']+)'",js)]
    blocks=re.split(r"id: '[dq]",js)[1:]
    for d,b in zip(days,blocks): d['steps']=len(re.findall(r"\{ type: '",b))
    units.append({'folder':folder,'grade':grade,'publisher':publisher,'unit':unit,'title':title,'days':days})
    page=src.replace('__TITLE__',title+' Daily').replace('__DATA__',did)
    out=os.path.join(gh,folder); os.makedirs(os.path.join(out,'data'))
    open(os.path.join(out,'index.html'),'w',encoding='utf-8').write(wrap(page))
    shutil.copy(os.path.join(R,'app.js'),out); shutil.copy(f,os.path.join(out,'data'))
    prev=re.sub(r'<script src="([^"]+)"></script>',lambda m:'<script>\n'+open(os.path.join(R,m.group(1)),encoding='utf-8').read()+'\n</script>',page)
    prev=prev.replace('<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n','')
    open(os.path.join(R,'dist','preview-'+folder+'.html'),'w',encoding='utf-8').write(prev)
    print('unit',folder,'|',grade,publisher,unit,title,[d['steps'] for d in days])
# 선생님 보드
BD=os.path.join(gh,SEC['board']); os.makedirs(BD)
hub=open(os.path.join(R,'hub.html'),encoding='utf-8').read().replace('__UNITS__',json.dumps(units,ensure_ascii=False)).replace('__BOARD__',SEC['board'])
open(os.path.join(BD,'index.html'),'w',encoding='utf-8').write(wrap(hub))
open(os.path.join(gh,'index.html'),'w',encoding='utf-8').write(wrap(open(os.path.join(R,'root.html'),encoding='utf-8').read().replace('</style>','</style>',1)))
json.dump(SEC,open(SP,'w'),indent=1)
print('BOARD', SEC['board'])
open(os.path.join(R,'dist','hub-units.json'),'w',encoding='utf-8').write(json.dumps(units,ensure_ascii=False))
json.dump({'name':'데일리 영어 보드','short_name':'데일리 영어','start_url':'./','scope':'./','display':'standalone',
  'background_color':'#f3f6f1','theme_color':'#2f5fd0','lang':'ko',
  'icons':[{'src':'icon-192.png','sizes':'192x192','type':'image/png'},{'src':'icon-512.png','sizes':'512x512','type':'image/png'},
           {'src':'icon-512.png','sizes':'512x512','type':'image/png','purpose':'maskable'}]},
  open(os.path.join(BD,'manifest.webmanifest'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
open(os.path.join(BD,'sw.js'),'w').write("""/* 앱 설치용 최소 서비스워커: 항상 새 버전을 먼저 받고, 인터넷이 끊기면 마지막 화면을 보여 준다 */
self.addEventListener('install', function (e) { self.skipWaiting(); });
self.addEventListener('activate', function (e) { e.waitUntil(self.clients.claim()); });
self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith(fetch(e.request).then(function (r) { var c = r.clone(); caches.open('daily-v1').then(function (k) { k.put(e.request, c); }); return r; })
    .catch(function () { return caches.match(e.request); }));
});
""")
for n in ('icon-192.png','icon-512.png'): shutil.copy(os.path.join(R,'tools',n),BD)
# README는 링크가 다 적혀 있어서 올리는 폴더에 넣지 않는다
