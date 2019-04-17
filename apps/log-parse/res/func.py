import os,sys,datetime

appLog = {}		# 用于存储log文件信息
kmsgLog = {}	# key为时间，value为文件名
TIMEFORMAT = '%m-%d %H:%M:%S.%f'
# 测试专用 #resultPath = os.path.join(os.path.split(os.getcwd())[0], 'result.cza')
resultPath = os.path.join(os.getcwd(),'result.cza')
def storeFile(filename):	# 根据log内容做定制，取特定时间信息
	start = filename.find('.')
	fileTime = filename[start+1:start+9]
	timeFormat = '%Y%m%d'
	time = datetime.datetime.strptime(fileTime,timeFormat)
	if filename.find('app-log') >= 0:
		appLog[time] = filename
	elif filename.find('kmsg-log') >= 0:
		kmsgLog[time] = filename
	else:
		print('there exist one error!')
		sys.exit()

def mergeApp(testPath, problemTime, searchRange): # 合并app-log
	appList = []	# 以列表形式存储log内容
	for index,filename in sorted(appLog.items(), key=lambda x: x[0], reverse=False):
		filename = os.path.join(testPath, filename)
		with open(filename,'r') as fr:
			context = fr.readlines()
			appList.append(context)
	with open(resultPath,'w') as fw:
		for context in appList:		# 此处内容为列表 --BUG?
			for temp in context:	# 故二次遍历
				end = temp.find(' ', temp.find('.'))
				lineTime = temp[:end] # 7是定制时定义好的距离
				if (datetime.datetime.strptime(lineTime,TIMEFORMAT) \
					- problemTime).seconds <= int(searchRange):
					temp = 'app****' + temp
					fw.write(temp)
				else:
					pass

def mergeKmsg(testPath, problemTime, searchRange): # 合并kmsg-log
	kmsgList = []
	for index,filename in sorted(kmsgLog.items(), key=lambda x: x[0], reverse=False):
		filename = os.path.join(testPath, filename)
		with open(filename,'r') as fr:
			context = fr.readlines()
			kmsgList.append(context)
	with open(resultPath,'a') as fw:
		for context in kmsgList:
			for temp in context:
				end = temp.find(' ', temp.find('.'))
				lineTime = temp[:end] # 7是定制时定义好的距离
				if (datetime.datetime.strptime(lineTime,TIMEFORMAT) \
					- problemTime).seconds <= int(searchRange):
					temp = 'kmsg***' + temp
					fw.write(temp)
				else:
					pass

def merge(): # 将app-log与kmsg-log混合合并，以时间排序
	logDict = {}
	with open(resultPath,'r') as fr:
		content = fr.readlines()
	with open(resultPath,'w') as fw:
		for line in content:
			end = line.find(' ', line.find('.')) # 找出完成的时间段
			time = line[7:end]
			time = datetime.datetime.strptime(time, TIMEFORMAT)
			logDict[time] = line
		for key,line in sorted(logDict.items(), key=lambda x:x[0], reverse=False):
			fw.write(line)
	print('merge done!')

def mergeLog(testPath, problemTime, searchRange): # API，合并函数入口
	ap_count,kmsg_count = 0,0
	for DIR,files,filenameList in os.walk(testPath):
		for filename in filenameList:
			if filename.find('app-log') >= 0:
				storeFile(filename)
				ap_count += 1
			elif filename.find('kmsg-log') >= 0:
				storeFile(filename)
				kmsg_count += 1
			else:
				pass
	
	# 判断字典内容是否为空，为空则表示物对应目标文件
	if appLog and kmsgLog is not None:
		print('restore done')
	else:
		print('not find aim log file')
		sys.exit()

	# 合并log文件
	problemTime = datetime.datetime.strptime(problemTime, '%m-%d %H:%M:%S')
	try:
		mergeApp(testPath,problemTime,searchRange)	# 合并app-log
		mergeKmsg(testPath,problemTime,searchRange)	# 合并kmsg-log
		merge()		# 针对ap，kmsg，进行混合合并，按时间顺序排序
	except:
		print('merge error')
		sys.exit()

	return ap_count,kmsg_count

# 内部测试
if __name__ == '__main__':
	testPath = os.path.join(os.path.split(os.getcwd())[0], 'test')
	problemTime = '12-30 14:58:0'
	searchRange = 300 # 5min is 300s
	mergeLog(testPath, problemTime, searchRange)