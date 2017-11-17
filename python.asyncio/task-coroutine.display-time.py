# -*- coding: utf-8 -*-

import asyncio
import datetime

"""
difference between base-event-loop:
  1. use async def
  2. use run until complete
  3. use sleep instead of call later
"""


async def display_date(_loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (_loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1.0)


loop = asyncio.get_event_loop()
"""
run until complete will receive a future object
display_date def with async way, so, this is an future like obj
"""
loop.run_until_complete(display_date(loop))
loop.close()
