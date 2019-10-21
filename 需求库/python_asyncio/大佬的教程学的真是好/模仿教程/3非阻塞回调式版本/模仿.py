import socket
import time

from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
stop_loop = 10


class Crawler:
    def __init__(self, flag=10):
        self.flag = flag
        self.sock = None
        self.response = b''

    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('www.baidu.com', 80))
        except BlockingIOError:
            pass
        selector.register(self.sock.fileno(), EVENT_WRITE, self.on_send)

    def on_send(self, sock):
        selector.unregister(sock.fd)
        self.sock.send(b'GET / HTTP/1.0\r\n\r\n')
        selector.register(self.sock.fileno(), EVENT_READ, self.on_recv)

    def on_recv(self, sock):
        chunk = self.sock.recv(1024)
        if chunk:
            self.response += chunk
        else:
            global stop_loop
            selector.unregister(sock.fd)
            print(self.response)
            stop_loop -= self.flag


def loop():
    while stop_loop:
        events = selector.select()
        for sock, mask in events:
            sock.data(sock)


def callback():
    Crawler().fetch()


def multi_callback(works=10):
    for _ in range(works):
        Crawler(1).fetch()


if __name__ == '__main__':
    start = time.time()
    # callback()
    multi_callback()
    loop()
    print(time.time() - start)
