import sys, json, importlib
sys.path.insert(0, '/home/claude/work/jd2610/gen')
import jfw
def build(mods):
    out = []
    for k, (mod, rng, story) in enumerate(mods):
        m = importlib.import_module(mod)
        out.append(jfw.spread(jfw.jday(m.p.n, 'DAY %d' % (k + 1), rng, story, m.p, m), m.p.n))
    return out
if __name__ == '__main__':
    for d in build([(a, a, a) for a in sys.argv[1:]]):
        print(d['id'], [(s['title'], len(s['items'])) for s in d['steps']])
