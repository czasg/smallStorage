import time,socket,threading

def tcplink(sock, addr):
	print('accept data from %s:%s' % addr)
	sock.send(b'Welcome to server')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('connect over')

address = ('127.0.0.1',9999)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)
print('server open..\nbegin wating for connetion...')

while True:
	sock, addr = s.accept()
	#print(sock, addr) #   127.0.0.1,54961
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()