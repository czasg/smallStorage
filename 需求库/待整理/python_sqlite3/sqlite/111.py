import os,sqlite3
"""
conn = sqlite3.connect('cza.db')
cursor = conn.cursor()
print('creating...')
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
print('create done!')
print('inserting...')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print('insert done!')

print(cursor.rowcount)

cursor.close() # 关闭游标
conn.commit() # 提交事物
conn.close() # 关闭connection
"""
if 'test.db' not in os.listdir():
	with open('test.db', 'w'):
		print('there is no db file\ncreate it now..')
		pass
try:
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	print('get db cursor')

	#sql = 'create table cza (id varchar(20) primary key, name varchar(20))'
	#cursor.execute(sql)
	#conn.commit()
	#print('create db tables success...')

	#sql = 'insert into cza (id, name) values (\'3\', \'Michae3\')'
	#cursor.execute(sql)
	#conn.commit()
	#print('insert one info success')

	sql = 'select * from cza'
	res = cursor.execute(sql)
	print(res.fetchall())

	cursor.close()
	conn.close()
	if 1 == 1:
		raise Exception('everything done')
		#raise 'everything done'
except Exception as e:
	print('error is %s' % e)