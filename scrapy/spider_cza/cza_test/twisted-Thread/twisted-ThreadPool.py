"""
为了将业务逻辑与事件分离，其中IO操作仍旧是异步的，但业务逻辑则采用线程来处理

"""
from twisted.internet import reactor, protocol
from twisted.protocols.basic import  LineReceiver

import time

class DemoProtocol(LineReceiver):
    def lineReceived(self, line):
        reactor.callInThread(self.hand_request,line)

    def hand_request(self):
        time.sleep(2)
        reactor.callFromThread(self.write_response,line)

    def write_response(self, result):
        self.transport.write('hello cza')

class DemoProtocolFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return DemoProtocol()

reactor.listenTCP(9090, DemoProtocolFactory())
reactor.run()

"""
deferToThread(self.handle_request, line).addCallback(self.write_resp)
开启一个线程执行处理IO等操作，然后添加一个回调函数来执行对应的结果

部分源码如下：
d = defer.Deferred()
def onResult(success, result):
    if success:
        reactor.callFromThread(d.callback, result)
    else:
        reactor.callFromThread(d.errback, result)
threadpool.callInThreadWithCallback(onResult)
return d

"""
