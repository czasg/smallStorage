from twisted.internet.defer import inlineCallbacks, Deferred, returnValue
from twisted.python.failure import Failure

from twisted.internet import reactor, defer


def loadRemoteData1(callbeck):
    import time
    time.sleep(1)
    print('11111')
    callbeck(1)

def loadRemoteData2(callback):
    import time
    time.sleep(2)
    print('22222')
    callback(2)

@defer.inlineCallbacks
def getRemoteData():
    d1 = defer.Deferred()
    reactor.callInThread(loadRemoteData1,d1.callback)
    print('now is 1')
    r1 = yield d1

    d2 = defer.Deferred()
    reactor.callInThread(loadRemoteData2,d2.callback)
    print('now is 2')
    r2 = yield d2

    returnValue(r1+r2)

def getResult(v):
    print('result is:',v)

if __name__ == '__main__':
    d = getRemoteData()
    d.addCallback(getResult)

    reactor.callLater(6, reactor.stop)
    reactor.run()