from twisted.internet import defer, reactor

def succeed(res):
    print('it succeed...',res)

def failure(res):
    print('it failure...',res)

def done(res):
    print('all done')

if __name__ == '__main__':
    deferList = []

    for i in range(3):
        d = defer.Deferred()
        d.addCallbacks(succeed, failure)
        deferList.append(d)

    defer.DeferredList(deferList).addBoth(done)  # it will wait all deferList complete the task and call their callback func, then it will execute it's callback func

    list = ['a','b','c']
    for i,j in enumerate(list):
        deferList[i].callback(j)
