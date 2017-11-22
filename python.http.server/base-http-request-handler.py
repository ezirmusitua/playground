# -*- coding: utf-8 -*-
from http.server import HTTPStatus, HTTPServer, BaseHTTPRequestHandler


class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<html><body><p>hello world</p></body></html>'.encode())


def run(server_class=HTTPServer, handler_class=DemoHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
    # use curl localhost:8000 to test
    # curl localhost:8000 will return
    # <html><body><p>hello world</p></body></html>
    # curl -XPOST will return 501, cause we did not implement do_POST
