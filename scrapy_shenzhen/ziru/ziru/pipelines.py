# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.http import Request
from ziru.img2num import img2num
from scrapy.pipelines.images import ImagesPipeline
import os,time
import requests
import pymysql

class ZiruPipeline(object):
    def __init__(self):
    	self.db = pymysql.connect("localhost","root","cza19950917","cza",charset = 'utf8')
    	self.cursor = self.db.cursor()

    def process_item(self, item, spider):
    	area = item['area']
    	eArea = item['eArea']
    	house = item['house']
    	price = item['price']
    	unit = item['unit']
    	print('insert data into database!')
    	sql = """insert into ziru_0_1(area,eArea,house,price,unit)VALUES(%s,%s,%s,%s,%s)"""
    	self.cursor.execute(sql,(area,eArea,house,price,unit))
    	self.db.commit()
    	print(area, eArea, house, price, unit)
    	print('insert done')
    	print('OK')