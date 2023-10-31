# to simplify our lives, we can use socketserver

import socket
import socketserver
import http.server
from http import HTTPStatus  # we don't want to remember statuses

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(HTTPStatus.OK)
        self.end_headers()

        page = "<html><body>Hello World - this is a Python Server</body></html>"
        self.wfile.write(page.encode())


httpd = socketserver.TCPServer(('127.0.0.1', 12345), Handler)
httpd.serve_forever()


