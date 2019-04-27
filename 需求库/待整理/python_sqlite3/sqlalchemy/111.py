from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() # 创建对象的基类

class User(Base):
	__tablename__ = 'user'

	id = Column(String(20), primary_key=True)
	name = Column(String(20))

print('connecting...')
engine = create_engine('mysql+mysqlconnector://root:cza19950917@localhost:3306/cza')
print('connect succeed...\n')
print('create session...')
DBSession = sessionmaker(bind=engine)
print('create done...')
print('-----------------start----------------------')
session = DBSession() # 创建session对象
new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()
print('-----------------done----------------------')
session = DBSession()
user = session.query(User).filter(User.id=='5').one()
print('type:',type(user))
print('name:',user.name)

session.close()