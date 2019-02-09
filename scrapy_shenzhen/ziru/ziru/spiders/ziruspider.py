# -*- coding: utf-8 -*-
import scrapy
from ziru.items import ZiruItem
from ziru.img2num import img2num
from scrapy.selector import Selector
from scrapy.http import Request
import re,os,shutil,time,random
import requests

class ZiruspiderSpider(scrapy.Spider):
    name = 'ziruspider'
    allowed_domains = ['ziroom']

    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'gr_user_id=676447e6-a86f-43d4-8786-0c4d93bf1589; SZ_nlist=%7B%2261492809%22%3A%7B%22id%22%3A%2261492809%22%2C%22sell_price%22%3A1890%2C%22title%22%3A%22%5Cu5357%5Cu5c71%5Cu533a%5Cu6d77%5Cu4e0a%5Cu4e16%5Cu754c2%5Cu53f7%5Cu7ebf%28%5Cu86c7%5Cu53e3%5Cu7ebf%29%5Cu6c34%5Cu6e7e%5Cu6d77%5Cu660c%5Cu5927%5Cu53a63%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1548942593%2C%22usage_area%22%3A10.2%2C%22floor%22%3A%225%22%2C%22floor_total%22%3A%227%22%2C%22room_photo%22%3A%22g2m1%5C%2FM00%5C%2F01%5C%2FDB%5C%2FChAFBlwScmmAY8IRAAkIorBCL_A864.jpg%22%2C%22city_name%22%3A%22%5Cu6df1%5Cu5733%22%7D%7D; __utm_source=pinzhuan; __utm_medium=baidu; ZIROOM_PHONE=9; gr_session_id_8da2730aaedd7628=df0f1a1f-89f2-4add-9c57-14c59dcced65; gr_session_id_8da2730aaedd7628_df0f1a1f-89f2-4add-9c57-14c59dcced65=true; mapType=%20; CURRENT_CITY_CODE=440300; CURRENT_CITY_NAME=%E6%B7%B1%E5%9C%B3',
            'Host': 'sz.ziroom.com',
            'Referer': 'http://sz.ziroom.com/z/nl/z3.html',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

    start_urls = ['http://sz.ziroom.com/z/nl/z3.html']

    def parse(self, response):
    	sel=Selector(response)
    	count = 0
    	temp = response.xpath('//*[@id="selection"]/div/div/dl[2]/dd/ul/li')

    	for i in range(1, len(temp)):
    		temp1 = temp[i].xpath('./div/span')
    		temp2 = temp[i].xpath('./span')
    		for j in range(1, len(temp1)):
    			count += 1
    			url = 'http:' + temp1[j].xpath('./a/@href').extract()[0]
    			area = temp2.xpath('./a/text()').extract()[0]
    			#//*[@id="selection"]/div/div/dl[2]/dd/ul/li[2]/span/a
    			eArea = temp1[j].xpath('./a/text()').extract()[0]
    			print(url, area, eArea)
    			yield scrapy.Request(url, meta={'area':area, 'eArea':eArea},callback=self.cparse, dont_filter=True)
    			#time.sleep(30)
    		print(count,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


    def cparse(self, response):
    	#delat time
    	delaytime = random.randint(5,8)
    	time.sleep(delaytime)

    	item = ZiruItem()
    	area = response.meta['area']
    	eArea = response.meta['eArea']

    	keys = r'image(.*):(.*)static8.ziroom.com(.*)phoenix(.*)png'
    	result = 'http:' + re.search(keys, response.text).group().split('"')[-1]
    	print(result, eArea)

        #new insert, add a re to get the house price
    	price_keys = r'image(.*):(.*)static8.ziroom.com(.*)phoenix(.*)png(.*)offset(.*)]]'
    	price_result = eval(re.search(price_keys, response.text).group().split(':')[-1])
    	print(price_result, type(price_result))

    	name = result.split('/')[-1]
    	filename = name.split('-1')[0]

    	try:
    		os.mkdir(os.path.join('D:\\ziru\\full', filename))
    	except:
    		shutil.rmtree(os.path.join('D:\\ziru\\full', filename))
    		os.mkdir(os.path.join('D:\\ziru\\full', filename))

    	url = result

    	r = requests.get(url)
    	with open('D:\\ziru\\full\\%s\\%s'%(filename, name),"wb") as f:
    		f.write(r.content)
    	print('down OK')

    	list = img2num('D:\\ziru\\full\\%s\\%s'%(filename, name))

    	print(list)

    	shutil.rmtree(os.path.join('D:\\ziru\\full', filename))

    	house_list = response.xpath('//*[@id="houseList"]/li')
    	for i in range(0, len(house_list)):
    		print(i, len(house_list))
    		# find each house name
    		house_name = house_list[i].xpath('./div[2]/h3/a/text()').extract()[0]
    		unit = house_list[i].xpath('./div[3]/p[1]/span/text()').extract_first().strip()#[0]

    		price_list = []
    		for j in range(len(price_result[i])):
    			price_list.append(price_result[i][j])

    		str_list = ''
    		for p in price_list:
    			str_list += str(list[p]) ###################################BUG######################################
    		price = int(str_list)#(list[one]) + str(list[two]) + str(list[three]) + str(list[four]))

    		item['area'] = area
    		item['eArea'] = eArea
    		item['house'] = house_name
    		item['price'] = price
    		item['unit'] = unit

    		yield item
    		#print('???????????????????')


    	# next url #
    	print('start next url')
    	pagenum = response.xpath('//div[@class="pages"]/a')
    	try:
    		if pagenum[-1].xpath('./text()').extract()[0] == '下一页':
    			#print(area, eArea)
    			print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    			next_url = 'http:' + pagenum[-1].xpath('./@href').extract()[0]
    			yield scrapy.Request(next_url, meta={'area':area, 'eArea':eArea}, callback=self.cparse, dont_filter=True)
    			print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           done            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    			print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')    	
    			print(next_url, area, eArea)
    	except:
    		pass