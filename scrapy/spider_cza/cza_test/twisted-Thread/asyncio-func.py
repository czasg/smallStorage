from twisted.internet import reactor,defer
import time

def func_1_time():
    print('11111111111111111')
    time.sleep(3)
    print('11111111111111111-done')
    return None

def func_1_handle(result):
    print('11111111111111111-all-done')

@defer.inlineCallbacks
def func_1():
    print('1 is running')
    d = defer.Deferred()
    reactor.callLater(2, d.callback, None)
    yield d
    print('1 result is ',d)
    yield defer.returnValue(1)

def func_2_time():
    print('22222222222222222')
    time.sleep(3)
    print('22222222222222222-done')
    return None

def func_2_handle(result):
    print('22222222222222222-all-done')

@defer.inlineCallbacks
def func_2():
    print('2 is running')
    d = defer.Deferred()
    reactor.callLater(3, d.callback, None)
    yield d
    print('2 result is ',d)
    yield defer.returnValue(3)

def main():
    d1 = func_1()
    d1.addCallback(func_1_handle)
    d2 = func_2()
    d2.addCallback(func_2_handle)

    def call_done(_):
        call_done.count += 1
        print('done one')
        if call_done.count == 2:
            reactor.stop()

    call_done.count = 0
    d1.addBoth(call_done)
    d2.addBoth(call_done)

reactor.callWhenRunning(main)
reactor.run()








