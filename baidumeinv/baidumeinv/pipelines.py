# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
#from scrapy import Request
import re

class BaidumeinvPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
    	for image_url in item['imgurl']:
    		print('++++++++++++++++++++++++++++++++')
    		print('++++++++++++++++++++++++++++++++')
    		print(image_url)
    		print(item['name'])
    		print(item['imgurl'])
    		print('++++++++++++++++++++++++++++++++')
    		print('++++++++++++++++++++++++++++++++')
    		yield Request(item['imgurl'],meta={'item':item['name']})
    
    def file_path(self, request, response=None, info=None):
    	name = request.meta['item']
    	name = re.sub(r'[？\\*|“<>:/()0123456789]', '', name)
    	image_guid = request.url.split('/')[-1]
    	filename = u'cza/{0}/{1}'.format(name, image_guid)
    	return filename
