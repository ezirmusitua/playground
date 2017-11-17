# -*- coding: utf-8 -*-

import asyncio


async def compute_with_1s_delay(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def compute_with_2s_delay(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y, compute):
    # wait for compute complete
    result = await compute(x, y)
    # then run this
    # how about insert something here ?
    print("%s + %s = %s" % (x, y, result))


async def end():
    await asyncio.sleep(3.0)


asyncio.ensure_future(print_sum(1, 2, compute_with_2s_delay))
asyncio.ensure_future(print_sum(2, 1, compute_with_1s_delay))
loop = asyncio.get_event_loop()
loop.run_until_complete(end())
loop.close()
