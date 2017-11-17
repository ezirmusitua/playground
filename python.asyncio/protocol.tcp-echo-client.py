# -*- coding: utf-8 -*-

import asyncio


# The base class for implementing streaming protocols
class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, _message, _loop):
        self.message = _message
        self.loop = _loop

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()


loop = asyncio.get_event_loop()

message = 'Hello World!'
"""
create_connection(
    protocol_factory,
    host=None,
    port=None,
    *,
    ssl=None,
    family=0,
    proto=0,
    flags=0,
    sock=None,
    local_addr=None,
    server_hostname=None
)
"""
coro = loop.create_connection(lambda: EchoClientProtocol(message, loop), '127.0.0.1', 8888)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()
