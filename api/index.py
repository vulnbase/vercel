from http.server import BaseHTTPRequestHandler

template = """
<html>
<body>
  <h1>Hello, World!</h1>
  <iframe src="https://webhooks.pw/test.html"></iframe>
</body>
</html>
"""

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(template.encode('utf-8'))
        return