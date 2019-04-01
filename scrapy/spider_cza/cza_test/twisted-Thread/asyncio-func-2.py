from twisted.internet  import reactor, defer
import time

def func_res(res):
    print('....',res)

def waste_func(x,callback):
    print('this is a wasting time func...')
    time.sleep(x)
    callback(1)

@defer.inlineCallbacks
def func1():
    print('now i am func1')
    d = defer.Deferred()
    # waste_func(3,d.callback)
    # yield waste_func(3,d.callback)
    reactor.callInThread(waste_func, 3, d.callback)
    # d.addCallback(func_res)
    yield d
@defer.inlineCallbacks
def func2():
    print('now i am func2')
    d = defer.Deferred()
    # waste_func(3,d.callback)
    reactor.callInThread(waste_func, 3, d.callback)
    # d.addCallback(func_res)
    yield d
@defer.inlineCallbacks
def func3():
    print('now i am func3')
    d = defer.Deferred()
    # waste_func(3,d.callback)
    reactor.callInThread(waste_func, 3, d.callback)
    # d.addCallback(func_res)
    yield d
@defer.inlineCallbacks
def func4():
    print('now i am func4')
    d = defer.Deferred()
    # waste_func(3,d.callback)
    reactor.callInThread(waste_func, 3, d.callback)
    # d.addCallback(func_res)
    yield d
@defer.inlineCallbacks
def func5():
    print('now i am func5')
    d = defer.Deferred()
    # waste_func(3,d.callback)
    reactor.callInThread(waste_func, 3, d.callback)
    # d.addCallback(func_res)
    yield d
def main():
    d1 = func1()
    d2 = func2()
    d3 = func3()
    d4 = func4()
    d5 = func5()

    def main_back(res):
        main_back.count += 1
        print('done one')
        if main_back.count == 5:
            print('main have done')
            reactor.stop()

    main_back.count = 0
    d1.addBoth(main_back)
    d2.addBoth(main_back)
    d3.addBoth(main_back)
    d4.addBoth(main_back)
    d5.addBoth(main_back)
if __name__ == '__main__':
    main()
    reactor.run()