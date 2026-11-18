# hwpx → t.txt (밑줄 charPr → <u>, lineBreak → 줄바꿈)
import re, sys
from xml.etree import ElementTree as ET
HP='{http://www.hancom.co.kr/hwpml/2011/paragraph}'
H=open('x/Contents/header.xml',encoding='utf-8').read()
ul={m.group(1) for m in re.finditer(r'<hh:charPr id="(\d+)"(.*?)</hh:charPr>',H,re.S) if (lambda u: u and u.group(1)!='NONE')(re.search(r'<hh:underline type="(\w+)"',m.group(2)))}
root=ET.fromstring(open('x/Contents/section0.xml',encoding='utf-8').read())
def ttext(t):
    out=t.text or ''
    for c in t:
        if c.tag==HP+'lineBreak': out+='\n'
        elif c.tag==HP+'tab': out+=' '
        out+=c.tail or ''
    return out
lines=[]
for p in root.iter(HP+'p'):
    s=''
    for r in p.findall(HP+'run'):
        txt=''.join(ttext(t) for t in r.findall(HP+'t'))
        if not txt: continue
        s+=('<u>'+txt+'</u>') if r.get('charPrIDRef') in ul and txt.strip() else txt
    lines.append(s)
open('t.txt','w',encoding='utf-8').write('\n'.join(lines))
