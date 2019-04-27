import socket

address = ('127.0.0.1',9999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
print('bind UDP on 9999...')

while True:
	data, addr = s.recvfrom(1024)
	print(addr)
	print('recv from %s:%s' % addr)
	s.sendto(b'Hello, %s' % data, addr)