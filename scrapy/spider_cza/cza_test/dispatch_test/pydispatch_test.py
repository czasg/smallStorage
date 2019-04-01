from pydispatch import dispatcher

def func():
    print("hello cza\'s world")

def trigger():
    print("i am czasg")

# hello = trigger()
# hello = object()
class cza:
    def __init__(self):
        print('i am cza')
hello = cza()

dispatcher.connect(func, signal=hello, sender=dispatcher.Anonymous)

dispatcher.send(signal=hello)
