# -*- coding: utf-8 -*-
from http.server import HTTPServer, BaseHTTPRequestHandler


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
    # use curl localhost:8000 to test
    # return 501 error, cause we did not implement the do_GET method
