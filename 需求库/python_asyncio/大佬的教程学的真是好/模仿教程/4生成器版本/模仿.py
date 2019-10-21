import socket
import time

from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
stop_loop = 10


class Future:
    def __init__(self):
        self.result = None
        self.callbacks = []

    def add_callback(self, func):
        self.callbacks.append(func)

    def set_result(self, result):
        self.result = result
        for func in self.callbacks:
            func(self)


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
        future = Future()

        def _on_send():
            future.set_result(None)

        selector.register(self.sock.fileno(), EVENT_WRITE, _on_send)
        yield future
        selector.unregister(self.sock.fileno())
        self.sock.send(b'GET / HTTP/1.0\r\n\r\n')
        while True:
            future = Future()

            def _on_recv():
                future.set_result(self.sock.recv(1024))

            selector.register(self.sock.fileno(), EVENT_READ, _on_recv)
            chunk = yield future
            selector.unregister(self.sock.fileno())
            if chunk:
                self.response += chunk
            else:
                global stop_loop
                stop_loop -= self.flag
                print(self.response)
                break


class Task:
    def __init__(self, co_routine):
        self.co_routine = co_routine
        future = Future()
        future.set_result(None)
        self.process(future)

    def process(self, future):
        try:
            next_future = self.co_routine.send(future.result)
        except StopIteration:
            return
        next_future.add_callback(self.process)


def loop():
    while stop_loop:
        events = selector.select()
        for sock, mask in events:
            sock.data()


def co_routine():
    Task(Crawler().fetch())


def multi_co_routines(works=10):
    for _ in range(works):
        Task(Crawler(1).fetch())


if __name__ == '__main__':
    start = time.time()
    # co_routine()
    multi_co_routines()
    loop()
    print(time.time() - start)
