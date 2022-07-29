import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

ext = ('html', 'png', 'pdf')

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path += "index.html"
        if not self.path.endswith(ext):
            self.path += ".html"
        SimpleHTTPRequestHandler.do_GET(self)

os.chdir("_site")
with HTTPServer(('', 8000), MyHandler) as server:
    server.serve_forever()
