import asyncio
"""
@asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行
把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
"""
@asyncio.coroutine
def hello():
    print("hello cza's world")
    yield from asyncio.sleep(1)
    print("hello again...")

loop = asyncio.get_event_loop()

loop.run_until_complete(hello())
loop.close()