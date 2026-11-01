import http.server, socketserver, pathlib, os, json, datetime, hashlib
ROOT = pathlib.Path(__file__).parent
PORT = 3002
os.chdir(ROOT)
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/v1/calculate':
            length = int(self.headers.get('content-length',0))
            data = json.loads(self.rfile.read(length) or b'{}')
            h = data.get('human_pct', 51)
            cert = {
                "id": f"SCDR-TOLUCA-GLOBAL-{hashlib.sha256(str(datetime.datetime.utcnow()).encode()).hexdigest()[:8]}",
                "human_pct": h,
                "ai_pct": 100-h,
                "voice_hash": data.get('voice_hash','pending'),
                "timestamp": datetime.datetime.utcnow().isoformat()+"Z",
                "chain_anchor": "ipfs://pending",
                "lifecycle": "ORIGINAL_ONLY",
                "lfd_compliance": True
            }
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            self.wfile.write(json.dumps(cert, indent=2).encode())
        else:
            self.send_error(404)
    def do_GET(self):
        if self.path.startswith('/api/v1/verify/'):
            cert_id = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"id": cert_id, "valid": True}).encode())
        else:
            return super().do_GET()
print(f"Sirviendo {ROOT} en http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
