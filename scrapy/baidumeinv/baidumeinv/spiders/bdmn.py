# -*- coding: utf-8 -*-
import scrapy
from baidumeinv.items import BaidumeinvItem
import re

class BdmnSpider(scrapy.Spider):
	name = 'bdmn'
	allowed_domains = ['www.umei.cc']
	start_urls = ['http://www.umei.cc/tags/dxmv.htm',
				'http://www.umei.cc/tags/lolita.htm',]

	def parse(self, response):
		list = response.css(".TypeList li")
		for img in list:
			imgname=img.css("a::text").extract_first()
			imgurl = img.css("a::attr(href)").extract_first()
			#imgurl2 = str(imgurl)
			print('pppppppppppppppppppppppppppppppppppp')
			print(imgname)
			print(imgurl)
			print('pppppppppppppppppppppppppppppppppppp')
			yield scrapy.Request(imgurl, callback=self.content)

	def content(self, response):
		item=BaidumeinvItem()
		item['name']=response.css(".ArticleTitle strong::text").extract_first()
		item['imgurl']=response.css(".ImageBody img::attr(src)").extract_first()
		print("***************************************")
		print("***************************************")
		print(item['name'])
		print(item['imgurl'])
		print("***************************************")
		print("***************************************")
		yield item

		next_url=response.css(".NewPages a::attr(href)").extract()
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		next_url=next_url[len(next_url)-1]
		temp = response.css(".next-pre a::attr(href)").extract_first()
		imgurl3 = temp.split('/')[-1]
		next_url=re.sub(imgurl3, next_url, temp)
		print(next_url)
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		if next_url is not None:
			print('??????????????????????????????????????????????????')
			print('??????????????????????????????????????????????????')
			yield response.follow(next_url,callback=self.content)
