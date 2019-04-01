from pydispatch import dispatcher

SIGNAL = 'my-first-signal'

def handle_event(sender):
    print('hello, cza\'s world', sender)


# The use of the Any object allows the handler to listen for messages from any Sender or to listen to Any message being sent.  To send messages:
dispatcher.connect(handle_event, signal=SIGNAL, sender=dispatcher.Any)

first_sender = object()
second_sender = {}

def main():
    dispatcher.send(signal=SIGNAL, sender=first_sender)
    dispatcher.send(signal=SIGNAL, sender=second_sender)

main()