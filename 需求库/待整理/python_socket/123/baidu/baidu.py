import socket

address = ('www.baidu.com',80)
keys = b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\nHost'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
s.send(keys)

buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer) #就是把他们连接起来嘛，神奇的操作
s.close()

header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('baidu.html','wb') as f:
	f.write(html)