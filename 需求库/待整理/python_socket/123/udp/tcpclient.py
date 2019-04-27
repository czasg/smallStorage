import socket

address = ('127.0.0.1',9999)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'cza', b'is', b'sg']:
	s.sendto(data, address)
	print(s.recv(1024).decode('utf-8'))
s.close()