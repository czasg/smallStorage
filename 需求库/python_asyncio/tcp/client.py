import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8878))
s.send('hello world'.encode())
print(s.recv(1024))