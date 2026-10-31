import re
base=open('wrapup-2509-22.html',encoding='utf-8').read()
_c=base[base.index('<style>'):base.index('</style>')]
_c=re.sub(r'@media \(max-width: 700px\) \{.*?\n\}\n', '', _c, flags=re.S)
css=_c+open('a4.css',encoding='utf-8').read()+'</style>\n'+open('a4.js',encoding='utf-8').read()
fonts=base[base.index('<link rel="preconnect"'):base.index('<style>')]
def Q(n,stem,body): return '\n  <div class="q">\n    <div class="stem"><span class="n">%d.</span>%s</div>\n%s\n  </div>\n'%(n,stem,body)
def OL(items,en=True): return '    <ol class="ol'+(' en' if en else '')+'">'+''.join('<li><span>%s</span><span>%s</span></li>'%(c,x) for c,x in zip('①②③④⑤',items))+'</ol>'
def TB(cols,rows): return '    <table class="ch"><thead><tr><th></th>'+''.join('<th>%s</th>'%c for c in cols)+'</tr></thead><tbody>'+''.join('<tr><td>%s</td>'%c+''.join('<td>%s</td>'%x for x in r)+'</tr>' for c,r in zip('①②③④⑤',rows))+'</tbody></table>'
BOX=lambda x:'    <div class="box"><p>'+x+'</p></div>'
GIV=lambda x:'    <div class="given">'+x+'</div>'
SUM=lambda x:'    <div class="sum">'+x+'</div>'
ORD=lambda: OL(['(A) − (C) − (B)','(B) − (A) − (C)','(B) − (C) − (A)','(C) − (A) − (B)','(C) − (B) − (A)'],False)
src=lambda x:'<span class="src">[%s]</span>'%x
