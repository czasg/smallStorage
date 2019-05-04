import asyncio
"""
@asyncio.coroutine -> async
yield from -> await
"""

@asyncio.coroutine
def wget(host):
    print("wget {}".format(host))
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = "GET / HTTP/1.0\r\nHOST: %s\r\n\r\n" % host
    writer.write(header.encode("UTF-8"))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print("{} header > {}".format(host, line.decode("utf-8").rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
