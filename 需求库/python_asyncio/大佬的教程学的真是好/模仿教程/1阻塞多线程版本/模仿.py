import socket
import time

from concurrent import futures


def blocking_socket():
    sock = socket.socket()
    sock.connect(('www.baidu.com', 80))
    sock.send(b'GET / HTTP/1.0\r\n\r\n')
    response = b''
    chunk = sock.recv(1024)
    while chunk:
        response += chunk
        chunk = sock.recv(1024)
    return response


def multi_blocking_socket(works=10):
    return [blocking_socket() for _ in range(works)].__len__()


def multi_threading(works=10):
    with futures.ThreadPoolExecutor(works) as executor:
        fs = [executor.submit(blocking_socket) for _ in range(works)]
    return [f.result() for f in fs].__len__()


if __name__ == '__main__':
    start = time.time()
    # print(blocking_socket())  # 单线程阻塞版本
    print(multi_blocking_socket())  # 单线程阻塞版本
    # print(multi_threading())  # 多线程阻塞版本
    print(time.time() - start)
