from twisted.internet import defer

def _func(info):
    print('hello cza:' + info)

result = 'this is a result'

# defer.succeed(result).addCallback(_func)

defer.succeed(result)

