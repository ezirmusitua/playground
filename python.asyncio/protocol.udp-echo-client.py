# -*- coding: utf-8 -*-
import asyncio


class EchoClientProtocol:
    def __init__(self, _message, _loop):
        self.message = _message
        self.loop = _loop
        self.transport = None

    def connection_made(self, _transport):
        self.transport = _transport
        print('Send:', self.message)
        self.transport.sendto(self.message.encode())

    def datagram_received(self, data):
        print("Received:", data.decode())

        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self):
        print("Socket closed, stop the event loop")
        _loop = asyncio.get_event_loop()
        _loop.stop()


loop = asyncio.get_event_loop()
message = "Hello World!"
"""
create_datagram_endpoint(
    protocol_factory,
    local_addr=None,
    remote_addr=None,
    *,
    family=0,
    proto=0,
    flags=0,
    reuse_address=None,
    reuse_port=None,
    allow_broadcast=None,
    sock=None
)
    socket family AF_INET or AF_INET6 depending on host (or family if specified), socket type SOCK_DGRAM.
    protocol_factory must be a callable returning a protocol instance.
    This method is a coroutine which will try to establish the connection in the background.
    When successful, the coroutine returns a (transport, protocol) pair.
    Options changing how the connection is created:
        local_addr, if given, is a (local_host, local_port) tuple used to bind the socket to locally.
            The local_host and local_port are looked up using getaddrinfo().
        remote_addr, if given, is a (remote_host, remote_port) tuple used to connect the socket to a remote address. 
            The remote_host and remote_port are looked up using getaddrinfo().
        family, proto, flags are the optional address family,
            protocol and flags to be passed through to getaddrinfo() for host resolution. 
            If given, these should all be integers from the corresponding socket module constants.
        reuse_address, tells the kernel to reuse a local socket in TIME_WAIT state,
            without waiting for its natural timeout to expire.
            If not specified will automatically be set to True on UNIX.
        reuse_port, tells the kernel to allow this endpoint to be bound to the same port as other existing endpoints 
            are bound to, so long as they all set this flag when being created.
            This option is not supported on Windows and some UNIX’s.
            If the SO_REUSEPORT constant is not defined then this capability is unsupported.
        allow_broadcast, tells the kernel to allow this endpoint to send messages to the broadcast address.
        sock, optionally be specified in order to use a preexisting,
            already connected, socket.socket object to be used by the transport.
            If specified, local_addr and remote_addr should be omitted (must be None).
            On Windows with ProactorEventLoop, this method is not supported.

See UDP echo client protocol and UDP echo server protocol examples.
"""
connect = loop.create_datagram_endpoint(lambda: EchoClientProtocol(message, loop), remote_addr=('127.0.0.1', 9999))
transport, protocol = loop.run_until_complete(connect)
loop.run_forever()
transport.close()
loop.close()
