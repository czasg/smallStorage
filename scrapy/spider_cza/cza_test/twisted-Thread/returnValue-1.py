from twisted.internet import reactor, defer

def handle_func():
    defer.returnValue('this is a return')

def handle_res(result):
    print(result)
    print('this res is from handle')

d = defer.Deferred()
# d.addCallback(handle_func)
defer.succeed(handle_func).addCallback(handle_res)
reactor.run()