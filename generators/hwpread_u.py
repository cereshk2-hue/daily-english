# 11/13 hwpread.py + 밑줄: DocInfo CHAR_SHAPE 의 밑줄 속성과 PARA_CHAR_SHAPE(글자 위치→모양)를 읽어 밑줄 구간을 U0 … U1 로 표시
import struct, zlib
from hwpread import ole
U0, U1 = '', ''
def recs(b):
    i = 0
    while i < len(b):
        h = struct.unpack_from('<I', b, i)[0]; i += 4
        tag = h & 0x3FF; size = h >> 20
        if size == 0xFFF: size = struct.unpack_from('<I', b, i)[0]; i += 4
        yield tag, b[i:i + size]; i += size
def text_u(path):
    f = ole(path)
    comp = struct.unpack_from('<I', f['FileHeader'], 36)[0] & 1
    dec = lambda b: zlib.decompress(b, -15) if comp else b
    under = []
    for tag, d in recs(dec(f['DocInfo'])):
        if tag == 21:   # CHAR_SHAPE
            attr = struct.unpack_from('<I', d, 46)[0]
            under.append(((attr >> 2) & 3) == 1)
    out = []
    secs = sorted([k for k in f if k.startswith('Section')], key=lambda k: int(k[7:]))
    for k in secs:
        pend = None
        for tag, d in recs(dec(f[k])):
            if tag == 67: pend = d
            elif tag == 68 and pend is not None:
                pairs = [struct.unpack_from('<II', d, j) for j in range(0, len(d), 8)]
                t = pend; s = []; j = 0; pos = 0; cur = False
                def shape_at(p):
                    sid = 0
                    for a, b in pairs:
                        if a <= p: sid = b
                        else: break
                    return under[sid] if sid < len(under) else False
                while j < len(t):
                    c = struct.unpack_from('<H', t, j)[0]
                    u = shape_at(pos)
                    if c in (1, 2, 3, 11, 12, 14, 15, 16, 17, 18, 21, 22, 23, 4, 5, 6, 7, 8, 9, 19, 20):
                        if c == 9: s.append('\t')
                        j += 16; pos += 8; continue
                    if c in (10, 13):
                        if cur: s.append(U1); cur = False
                        if c == 10: s.append('\n')
                        j += 2; pos += 1; continue
                    ch = '-' if c == 24 else ' ' if c in (30, 31) else chr(c)
                    if u and not cur and ch.strip(): s.append(U0); cur = True
                    elif not u and cur: s.append(U1); cur = False
                    s.append(ch); j += 2; pos += 1
                if cur: s.append(U1)
                out.append(''.join(s)); pend = None
        if pend is not None: pass
    return '\n'.join(out)
if __name__ == '__main__':
    import sys; print(text_u(sys.argv[1]))
