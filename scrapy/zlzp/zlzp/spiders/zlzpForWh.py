# -*- coding: utf-8 -*-
import scrapy
import re,json,time,random
from zlzp.items import ZlzpItem

class ZlzpforwhSpider(scrapy.Spider):
    name = 'zlzpForWh'
    allowed_domains = ['fe-api.zhaopin.com']
    fornt = 'https://fe-api.zhaopin.com/c/i/sou?start={0}&pageSize={1}&cityId={2}&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%89%8D%E7%AB%AF&kt=3&_v=0.92358882&x-zp-page-request-id=1dcbcc1f5cd943baa58207b4dfc8ae37-1551184086163-212025'
    back = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize={}&cityId=736&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%90%8E%E7%AB%AF&kt=3&_v=0.92358882&x-zp-page-request-id=1dcbcc1f5cd943baa58207b4dfc8ae37-1551184086163-212025'
    start,pageSize = 0,100
    start_urls = ['https://sou.zhaopin.com/?jl=736&kw=%E5%89%8D%E7%AB%AF&kt=3']#fornt.format(0,100)]#, back.format(0,100)]

    def parse(self, response):
    	#ajax_dict = json.loads(response.text)
    	print('##########################################')
    	keys = r'"currentCityInfo":(.*),"metro"'
    	re_content = eval(re.search(keys, response.text).group(1) + '}')
    	city_id,city_name,city_list = re_content['code'],re_content['name'],re_content['sublist']
    	#print(city_id,'\n',city_name,'\n',city_list)
    	flag = 0
    	while flag < 10:
    		for i in range(len(city_list)):
    			child_id,child_name = city_list[i]['code'],city_list[i]['name']
    			print(child_id, child_name)
    			#print(self.fornt.format(start,pageSize,child_id))
    			yield scrapy.Request(self.fornt.format(self.start,self.pageSize,child_id), meta={'child_id':child_id,'type':'fornt'}, callback=self.parse2, dont_filter=True)
    			#print('@'*12)
    			yield scrapy.Request(self.back.format(self.start,self.pageSize,child_id), meta={'child_id':child_id,'type':'back'}, callback=self.parse2, dont_filter=True)
    			#self.start,self.pageSize += self.pageSize,self.pageSize+100
    			print(self.start,self.pageSize)
    		time.sleep(2)
    		flag += 1
    		self.start,self.pageSize = self.pageSize,self.pageSize+100

    #filter error, need to add dont_filter
    def parse2(self, response):
    	delaytime = random.randint(5,8)
    	time.sleep(delaytime)
    	ajax_dict = json.loads(response.text)
    	item = ZlzpItem()
    	if response.meta['type'] == 'fornt':
    		for ajax in range(len(ajax_dict['data']['results'])):
    			item['name'] = ajax_dict['data']['results'][ajax]['jobName']
    			item['place'] = ajax_dict['data']['results'][ajax]['city']['display']
    			item['salary'] = ajax_dict['data']['results'][ajax]['salary']
    			item['child_id'] = response.meta['child_id']
    			item['type_s'] = 'fornt'
    			print(item['name'],item['place'],item['salary'])
    			yield item
    	elif response.meta['type'] == 'back':
    		for ajax in range(len(ajax_dict['data']['results'])):
    			item['name'] = ajax_dict['data']['results'][ajax]['jobName']
    			item['place'] = ajax_dict['data']['results'][ajax]['city']['display']
    			item['salary'] = ajax_dict['data']['results'][ajax]['salary']
    			item['child_id'] = response.meta['child_id']
    			item['type_s'] = 'back'
    			print(item['name'],item['place'],item['salary'])
    			yield item
    	#print(type(re_content))
    	#for i in range(0, len(each_place)):
    	#	print(i)
    	#	print(each_place[i].xpath('./a/@href').extract()[0])

#//*[@id="queryCityBox"]/div/div/ul/li[2]
#//*[@id="search"]/div[3]/div[2]/div/ul/li[2]
"""
{"parent":"736","code":"736","name":"武汉","sublist":
[{"name":"武汉吴家山经济技术开发区","en_name":"Wujiashan","code":"2367","sublist":[]},
{"name":"东湖新技术开发区","en_name":"Donghuxinqu","code":"2366","sublist":[]},
{"name":"武汉经济技术开发区","en_name":"Jingjikaifaqu","code":"2365","sublist":[]},
{"name":"江夏区","en_name":"Jiangxia","code":"2067","sublist":[]},
{"name":"汉南区","en_name":"Hannan","code":"2066","sublist":[]},
{"name":"东西湖区","en_name":"Dongxihu","code":"2065","sublist":[]},
{"name":"蔡甸区","en_name":"Caidian","code":"2064","sublist":[]},
{"name":"洪山区","en_name":"Hongshan","code":"2063","sublist":[]},
{"name":"青山区","en_name":"Qingshan","code":"2062","sublist":[]},
{"name":"武昌区","en_name":"Wuchang","code":"2061","sublist":[]},
{"name":"汉阳区","en_name":"Hanyang","code":"2060","sublist":[]},
{"name":"硚口区","en_name":"Changkou","code":"2059","sublist":[]},
{"name":"江汉区","en_name":"Jianghan","code":"2058","sublist":[]},
{"name":"江岸区","en_name":"Jiangan","code":"2057","sublist":[]},
{"name":"新洲区","en_name":"Xinzhou","code":"2069","sublist":[]},
{"name":"黄陂区","en_name":"Huangpo","code":"2068","sublist":[]}]}
"""