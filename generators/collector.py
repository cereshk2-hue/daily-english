from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class H(BaseHTTPRequestHandler):
    def do_POST(self):
        b=self.rfile.read(int(self.headers['Content-Length'])); d=json.loads(b)
        for r in d['rows']: open('/tmp/claude-0/-home-claude/a9e3e882-1f02-5d62-8f70-aced81bc59d2/scratchpad/rows.jsonl','a').write(json.dumps(r,ensure_ascii=False)+'\n')
        self.send_response(200); self.send_header('Access-Control-Allow-Origin','*'); self.end_headers(); self.wfile.write(b'ok')
    def log_message(self,*a): pass
HTTPServer(('',8766),H).serve_forever()
