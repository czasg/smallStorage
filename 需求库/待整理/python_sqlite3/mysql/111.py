import mysql.connector

conn = mysql.connector.connect(
	user='root',
	password='cza19950917',
	database='cza')
cursor = conn.cursor()
print('creating...')
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
print('create done...')
print('inserting...')
cursor.execute('insert into user (id, name) values (%s,%s)',['1','Michael'])
print('insert done...')

conn.commit()
cursor.close()
print('---------------------------------------------')
print('begin finding...')
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))

values = cursor.fetchall()
print(values)
print('done!')
cursor.close()
conn.close()
print('all close!')