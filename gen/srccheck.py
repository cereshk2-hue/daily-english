import json, subprocess, re, sys
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('…', '...')
    s = re.sub(r'[①-⑳]', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()
units = {
 'm1-donga-yoon-L6.js': (['hwp17/x.txt', 'hwpscan/6e9e2346-2022__2025___1_______7__01_________4.hwp.txt', 'hwp15/x.txt'], ['c6a','c6b','c7a','c7b','c5a','c5b','L5a','L5b']),
 'm1-chunjae-so-L6.js': (['hwp13/x.txt', 'hwp14/x.txt', 'hwp16/x.txt'], ['k4a','k4b','k5a','k5b','k6a','k6b']),
 'm3-jihak-min-L7.js': (['hwp18/x.txt', 'hwp19/x.txt'], ['j7a','j7b','j7c','j8a','j8b','j8c']),
 'm2-visang-hwang-L7.js': (['hwp20/x.txt'], ['v7a','v7b']),
}
bad = 0
for f, (srcs, ids) in units.items():
    src = norm(' '.join(open(s).read() for s in srcs))
    srcj = src.replace(' ', '')
    PK = json.loads(subprocess.check_output(['node', '-e', "global.window={};require('/home/claude/proj/data/%s');process.stdout.write(JSON.stringify(window.PKG))" % f]))
    for d in PK['days']:
        if d['id'] not in ids: continue
        for l in d['passage']:
            if l[0] == '#' or (not l[0] and re.match(r'^[❶-❿]$', l[1])): continue
            for part, lab in ((l[1], 'EN'), (l[2], 'KO')):
                for sent in re.split(r'(?<=[.!?])\s+', part):
                    n = norm(sent)
                    if not n: continue
                    if n in src or n.replace(' ', '') in srcj: continue
                    bad += 1; print(f, d['id'], lab, '|', sent)
print('mismatch', bad)
