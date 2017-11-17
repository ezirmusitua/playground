# -*- coding: utf-8 -*-

import asyncio
import datetime


def display_date(_end_time, _loop):
    print(datetime.datetime.now())
    if (_loop.time() + 1.0) < _end_time:
        _loop.call_later(1, display_date, _end_time, _loop)
    else:
        _loop.stop()


loop = asyncio.get_event_loop()

# Schedule the first call to display_date()
end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()