import time,datetime

FILENAME = ['app-log.20181228','kmsg-log.20181228']

for i in range(2):
	fileName = FILENAME[i]
	with open(fileName,'w') as fw:
		for j in range(1000):
			content = '12-28 14:58:{}.{}'.format(i,j)
			fw.write(content + ' ' + 'cza is sg' + '\n')