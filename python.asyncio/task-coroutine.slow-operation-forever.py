# -*- coding: utf-8 -*-

import asyncio


async def slow_operation(_future):
    await asyncio.sleep(1)
    _future.set_result('Future is done!')


def got_result(_future):
    print(_future.result())
    loop.stop()


loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
# done callback, what will do after the future is done
future.add_done_callback(got_result)

try:
    loop.run_forever()
finally:
    loop.close()
