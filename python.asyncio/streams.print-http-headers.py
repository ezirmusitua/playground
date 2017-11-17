# -*- coding: utf-8 -*-

import asyncio
import urllib.parse
import sys


@asyncio.coroutine
async def print_http_headers(_url):
    _url = urllib.parse.urlsplit(_url)
    if _url.scheme == 'https':
        connect = asyncio.open_connection(_url.hostname, 443, ssl=True)
    else:
        connect = asyncio.open_connection(_url.hostname, 80)
    reader, writer = await connect
    query = 'HEAD {path} HTTP/1.0\r\nHost: {hostname}\r\n\r\n'.format(path=_url.path or '/', hostname=_url.hostname)
    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break
        line = line.decode('latin1').rstrip()
        if line:
            print('HTTP header> %s' % line)

    # Ignore the body, close the socket
    writer.close()


try:
    url = sys.argv[1]
except IndexError:
    url = 'https://httpbin.org/get'
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(print_http_headers(url))
loop.run_until_complete(task)
loop.close()
