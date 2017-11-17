# -*- coding: utf-8 -*-

import asyncio


async def slow_operation(_future):
    await asyncio.sleep(1)
    _future.set_result('Future is done!')


loop = asyncio.get_event_loop()

# key points
future = asyncio.Future()
# ensure_future
# schedule coroutine execution
asyncio.ensure_future(slow_operation(future))
loop.run_until_complete(future)

print(future.result())
loop.close()
