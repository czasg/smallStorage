# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class ZlzpPipeline(object):
    def __init__(self):
    	self.db = sqlite3.connect('zlzp.db')
    	self.cursor = self.db.cursor()

    def process_item(self, item, spider):
    	name = item['name']
    	place = item['place']
    	salary = item['salary']
    	child_id = item['child_id']
    	type_s = item['type_s']
    	print('insert data into database!')
    	sql = """insert into zlzp(name,place,salary,child_id,type_s)VALUES('%s','%s','%s','%s','%s')"""
    	self.cursor.execute(sql % (name,place,salary,child_id,type_s))
    	self.db.commit()
    	print('insert done')
    	print('OK')
#create table zlzp(name varchar(50), place varchar(50), salary varchar(50))