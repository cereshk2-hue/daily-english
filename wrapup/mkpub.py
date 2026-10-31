import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read(); i = s.index('<main>')
open(dst, 'w', encoding='utf-8').write('<!DOCTYPE html>\n<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n' + s[:i].replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '') + '</head><body>\n' + s[i:] + '</body></html>\n')
