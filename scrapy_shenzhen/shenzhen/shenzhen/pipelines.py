# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from shenzhen.items import ShenzhenItem

region = ['福田','罗湖','南山','盐田','宝安','龙岗','坪山','光明','龙华','大鹏']
region_cityID = [2037,2038,2039,2040,2041,2042,2043,2044,2361,2362]
region_cityID_dict = {'2037':0,'2038':0,'2039':0,'2040':0,'2041':0,'2042':0,'2043':0,'2044':0,'2361':0,'2362':0}
mysql_tag = 0

class ShenzhenPipeline(object):
    def __init__(self):
    	self.db = pymysql.connect("localhost","root","cza19950917","cza",charset = 'utf8')
    	self.cursor = self.db.cursor()

    def process_item(self, item, spider):
    	global mysql_tag
    	if item['tag'] is None:
    		if mysql_tag == 0:
    			sql = """drop table if exists shenzhen"""
    			self.cursor.execute(sql)
    			self.db.commit()
    			sql = """create table shenzhen(job_salary varchar(10),job_site varchar(10),job_exp varchar(10))"""
    			self.cursor.execute(sql)
    			self.db.commit()
    			mysql_tag += 1
    		sql = """insert into shenzhen(job_salary,job_site,job_exp)VALUES(%s,%s,%s)"""
    		data = (item['job_salary'],item['job_site'],item['job_exp'])
    		self.cursor.execute(sql,data)
    		self.db.commit()
    	else:
    		if region_cityID_dict[str(item['tag'])] == 0:
    			sql = """drop table if exists t_%s"""
    			self.cursor.execute(sql,item['tag'])
    			self.db.commit()
    			sql = """create table t_%s(job_salary varchar(10),job_site varchar(10),job_exp varchar(10))"""
    			self.cursor.execute(sql,item['tag'])
    			self.db.commit()
    			region_cityID_dict[str(item['tag'])] += 1
    		sql = """insert into t_%s(job_salary,job_site,job_exp)VALUES(%s,%s,%s)"""
    		data = (item['tag'],item['job_salary'],item['job_site'],item['job_exp'])
    		self.cursor.execute(sql,data)
    		self.db.commit()
        return item
    def close_db(self):
    	self.cursor.close()
    	self.db.close()