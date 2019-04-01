from twisted.internet import reactor, defer

def process_chain(callbacks, input, *a, **kwargs):
    d = defer.Deferred()
    for callback in callbacks:
        d.addCallback(callback, *a, **kwargs)
    d.callback(input)
    return d

def first(res):
    res_new = res + 1
    print('first:','old is:',res,' and the new is:',res_new)
    return res_new

def second(res):
    res_new = res + 1
    print('first:', 'old is:', res, ' and the new is:', res_new)
    return res_new

if __name__ == '__main__':
    callbacks = [first, second]
    input = 1
    res = process_chain(callbacks, input)
    print('all done', type(res))