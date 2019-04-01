from twisted.internet import defer

def myCallback(info):
    print('this is info from callback:'
          + '\n' + info)

d = defer.Deferred()
d.addCallback(myCallback)
d.callback('cza') # 这里传入的是回调的结果？
# 所以他的意思就是主动唤醒回调函数，即使没有主函数完成
# 我也能够主动传递一个假信息，来提前触发他的回调执行吗？