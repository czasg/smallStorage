from twisted.internet import defer, reactor
from twisted.web.client import getPage, Agent, downloadPage
"""getPage是获取页面返回str，而downloadPage是下载页面并保存到对应文件的"""


def succeed(res):
    print('getPage succeed')
    print(res)

def failure(res):
    print('getPage failure')
    print(res)

def stop(_):
    print('all done')
    reactor.stop()

if __name__ == '__main__':
    d = getPage(b'http://www.baidu.com')
    d.addCallbacks(succeed, failure)
    # d.addCallback(succeed)
    d.addBoth(stop)
    reactor.run()
