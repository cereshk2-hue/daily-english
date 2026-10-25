import struct, sys, zlib

def ole(path):
    d = open(path, 'rb').read()
    ss = 1 << struct.unpack_from('<H', d, 30)[0]
    mss = 1 << struct.unpack_from('<H', d, 32)[0]
    nfat, dirstart = struct.unpack_from('<II', d, 44)
    minicut, minifat, nmini, difat, ndifat = struct.unpack_from('<IIIII', d, 56)
    sec = lambda i: d[512 + i * ss: 512 + (i + 1) * ss]
    fatsecs = list(struct.unpack_from('<109I', d, 76))
    nx = difat
    while nx not in (0xFFFFFFFE, 0xFFFFFFFF) and ndifat:
        s = sec(nx); vals = struct.unpack('<%dI' % (ss // 4), s)
        fatsecs += vals[:-1]; nx = vals[-1]; ndifat -= 1
    fat = []
    for f in fatsecs[:nfat]:
        fat += struct.unpack('<%dI' % (ss // 4), sec(f))
    def chain(s):
        out = []
        while s < 0xFFFFFFFA:
            out.append(s); s = fat[s]
        return out
    rd = lambda s: b''.join(sec(i) for i in chain(s))
    dirs = rd(dirstart)
    ents = []
    for i in range(len(dirs) // 128):
        e = dirs[i * 128:(i + 1) * 128]
        nl = struct.unpack_from('<H', e, 64)[0]
        name = e[:max(nl - 2, 0)].decode('utf-16le')
        typ = e[66]
        start, size = struct.unpack_from('<IQ', e, 116)
        ents.append((name, typ, start, size & 0xFFFFFFFF))
    root = ents[0]
    ministream = rd(root[2])
    mfat = []
    for i in chain(minifat):
        mfat += struct.unpack('<%dI' % (ss // 4), sec(i))
    def mread(s, size):
        out = b''
        while s < 0xFFFFFFFA:
            out += ministream[s * mss:(s + 1) * mss]; s = mfat[s]
        return out[:size]
    files = {}
    for name, typ, start, size in ents:
        if typ == 2:
            files[name] = mread(start, size) if size < minicut else rd(start)[:size]
    return files

def text(path):
    f = ole(path)
    hdr = f['FileHeader']
    comp = struct.unpack_from('<I', hdr, 36)[0] & 1
    out = []
    secs = sorted([k for k in f if k.startswith('Section')], key=lambda k: int(k[7:]))
    for k in secs:
        b = f[k]
        if comp: b = zlib.decompress(b, -15)
        i = 0
        while i < len(b):
            h = struct.unpack_from('<I', b, i)[0]; i += 4
            tag = h & 0x3FF; size = h >> 20
            if size == 0xFFF: size = struct.unpack_from('<I', b, i)[0]; i += 4
            if tag == 67:
                t = b[i:i + size]; s = []; j = 0
                while j < len(t):
                    c = struct.unpack_from('<H', t, j)[0]
                    if c in (1, 2, 3, 11, 12, 14, 15, 16, 17, 18, 21, 22, 23):
                        j += 16; continue
                    if c in (4, 5, 6, 7, 8, 9, 19, 20):
                        j += 16 if c not in (9,) else 16
                        if c == 9: s.append('\t')
                        continue
                    if c == 10 or c == 13: s.append('\n') if c == 10 else None; j += 2; continue
                    if c == 24: s.append('-'); j += 2; continue
                    if c in (30, 31): s.append(' '); j += 2; continue
                    s.append(chr(c)); j += 2
                out.append(''.join(s))
            i += size
    return '\n'.join(out)

sys.stdout.write(text(sys.argv[1]).encode("utf-16","surrogatepass").decode("utf-16","replace")+"\n")
