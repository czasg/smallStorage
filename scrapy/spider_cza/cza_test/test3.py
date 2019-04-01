from twisted.internet import reactor, defer
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

class resourceShow(Protocol):
    def __init__(self, res):
        self.res = res
    def dataReceived(self, data):
        print('next info from Protocol')
        print('data from res:',type(data), )
    def connectionLost(self, reason):
        self.res.callback(None)

def test(_):
    print('????????????????')

def succeed(res):
    print('agent get html succeed...')
    d = defer.Deferred(test)
    res.deliverBody(resourceShow(d))
    return d

def failure(_):
    print('it failure...')
    print('breack out')

def stop(_):
    print('all done')
    reactor.stop()

if __name__ == '__main__':
    agent = Agent(reactor)
    d = agent.request(b'GET',
                      b'http://www.baidu.com',)
                      # headers=Headers({'User-Agent':['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36']}))
    d.addCallbacks(succeed, failure)
    d.addBoth(stop)
    reactor.run()
