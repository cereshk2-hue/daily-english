# hwpx → 글자 (hwpread_u 와 같은 형식: 밑줄 구간  … , lineBreak → 줄바꿈, 문단 = 한 줄)
import re, sys, zipfile
from xml.etree import ElementTree as ET
HP = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'
z = zipfile.ZipFile(sys.argv[1])
H = z.read('Contents/header.xml').decode('utf-8')
ul = {m.group(1) for m in re.finditer(r'<hh:charPr id="(\d+)"(.*?)</hh:charPr>', H, re.S) if (lambda u: u and u.group(1) != 'NONE')(re.search(r'<hh:underline type="(\w+)"', m.group(2)))}
secs = sorted(n for n in z.namelist() if re.match(r'Contents/section\d+\.xml', n))
def ttext(t):
    out = t.text or ''
    for c in t:
        if c.tag == HP + 'lineBreak': out += '\n'
        elif c.tag == HP + 'tab': out += '\t'
        out += c.tail or ''
    return out
lines = []
for sn in secs:
    root = ET.fromstring(z.read(sn).decode('utf-8'))
    for p in root.iter(HP + 'p'):
        s = ''
        for r in p.findall(HP + 'run'):
            txt = ''.join(ttext(t) for t in r.findall(HP + 't'))
            if not txt: continue
            s += ('' + txt + '') if r.get('charPrIDRef') in ul and txt.strip() else txt
        lines.append(s)
print('\n'.join(lines))
