# -*- coding: utf-8 -*-

import asyncio
import functools
import os
import signal


# listen signal, for kill by Ctrl + C
def ask_exit(_signame):
    print('\nGot Signal %s: EXIT' % _signame)
    loop.stop()


loop = asyncio.get_event_loop()
for signame in ('SIGINT', 'SIGTERM'):
    loop.add_signal_handler(getattr(signal, signame), functools.partial(ask_exit, signame))

print('Event loop running forever, press Ctrl+C to interrupt.')
print('PID %s: send SIGINT or SIGTERM to exit. ' % os.getpid())

try:
    loop.run_forever()
finally:
    loop.close()
