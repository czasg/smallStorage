from pydispatch import dispatcher

SIGNAL_A = 'A'
SIGNAL_X = 'X'

def handle_event_a(sender):
    print('hello, this is from a')
    print(sender)

def handle_event_b(sender):
    print('hello, this is from b')
    print(sender)

if __name__ == '__main__':
    dispatcher.connect(handle_event_a, signal=SIGNAL_A, sender=dispatcher.Any)
    dispatcher.connect(handle_event_b, signal=SIGNAL_A, sender=dispatcher.Any)
    dispatcher.send(SIGNAL_A, {"huawei":"honer"})
    # dispatcher.send(SIGNAL_A, {"apple":"iphone"})
    # dispatcher.send(signal=SIGNAL_A, sender={})