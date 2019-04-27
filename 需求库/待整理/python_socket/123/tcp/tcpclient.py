import socket

address = ('127.0.0.1',9999)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
print(s.recv(1024).decode('utf-8'))

for data in [b'cza', b'is', b'sg']:
	print('sending msg..')
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
	print('recv done')
s.send(b'exit')
s.close()