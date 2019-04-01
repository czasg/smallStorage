from twisted.internet import task
from twisted.internet import reactor
import time

def runVerySecond():
    print('hello,it is {} now'.format(time.time()))

if __name__ == '__main__':
    aim = task.LoopingCall(runVerySecond)
    aim.start(2)

    reactor.callLater(8, reactor.stop)
    reactor.run()