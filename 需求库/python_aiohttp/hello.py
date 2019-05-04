import asyncio

from aiohttp import web
"""
这就干出来了一个小服务器，还是加了时延的

"""

async def index(request):
    print('a request to index')
    await asyncio.sleep(1)
    return web.Response(body=b"<h1>Index</h1>", content_type='text/html')

async def hello(request):
    print('a request to hello')
    await asyncio.sleep(1)
    text = "<h1>hello, %s</h1>" % request.match_info["name"]
    return web.Response(body=text.encode("utf-8"), content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9999)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()