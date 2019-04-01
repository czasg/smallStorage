from twisted.internet import reactor, defer

def f():
    pass

def func():
    return f()

@defer.inlineCallbacks
def process_data():
    d = defer.Deferred()
    print('running...')
    yield func()
    print('can go here?')
    d.callback()
    reactor.stop()

if __name__ == '__main__':
    process_data()
    reactor.run()
