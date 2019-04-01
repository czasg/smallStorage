from twisted.internet import reactor, defer

class Test(object):
    def create(self, info):
        self.d = defer.Deferred()
        reactor.callLater(1, self._process_info, info)
        self.d.addCallback(self._toHTML)
        return self.d

    def _process_info(self, info):
        if len(info) > 50:
            self.d.errback(Exception('there is an error'))
        else:
            self.d.callback(info)

    def _toHTML(self, info):
        return ('<h1>' + info + '</h1>')

def onSuccess(info):
    print('info success:' + info)
    reactor.stop()

def onFailure(info):
    print('info failure:' + info)
    reactor.stop()

d = Test()
d = d.create('czaczaczacza'*10)
d.addCallbacks(onSuccess, onFailure)

reactor.run()