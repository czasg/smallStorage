import asyncio
import threading


@asyncio.coroutine
def hello():
    print("hello, {}".format(threading.currentThread()))
    yield from asyncio.sleep(2)
    print("hello, {}".format(threading.currentThread()))


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

