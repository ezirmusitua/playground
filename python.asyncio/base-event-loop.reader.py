# -*- coding: utf-8 -*-

import asyncio

try:
    from socket import socketpair
except ImportError:
    from asyncio.windows_utils import socketpair

# Create a pair of connected file descriptors
read_sock, write_sock = socketpair()
loop = asyncio.get_event_loop()


def reader():
    data = read_sock.recv(100)
    data_decoded = data.decode()
    print("Received: ", data.decode())
    if data_decoded == '---abc':
        # We are done: un register the file descriptor
        loop.remove_reader(read_sock)
        # Stop the event loop
        loop.stop()


# Register the file descriptor for read event
loop.add_reader(read_sock, reader)

# Simulate the reception of data from the network

loop.call_soon(write_sock.send, '---def'.encode())
loop.call_later(5.0, write_sock.send, '---abc'.encode())

# Run the event loop
loop.run_forever()

# We are done, close sockets and the event loop
read_sock.close()
write_sock.close()
loop.close()
