# -*- coding: utf-8 -*-

import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))


loop = asyncio.get_event_loop()

# what is asyncio.gather?
"""
asyncio.gather(*coros_or_futures, loop=None, return_exceptions=False)
  将传入的 coroutine/futures 聚合成为一个 future
  所有的 future 必须使用同一个 event loop(也就是说在同一个 program 里可以有多个 event loop 咯)
  如果所有的 task 都完成了,返回结果是结果的列表(传入顺序)
  如果设置了 return_exceptions,那么即使有异常,任务中异常的结果也会被成功返回
  没有设置的花,第一个被抛出的异常会立刻抛出otherwise, the first raised exception will be immediately propagated to the returned future.

  如何取消:
  gathered Future 被取消,所有子 future 取消
  子 future 取消,抛出 CancelledError,但不会取消 gathered Future
"""
# how factorial became task? - cause this is an async function, bcs
loop.run_until_complete(asyncio.gather(
    factorial("A", 2),
    factorial("B", 3),
    factorial("C", 4),
))

loop.close()
