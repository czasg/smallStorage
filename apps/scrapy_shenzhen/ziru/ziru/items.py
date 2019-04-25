# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZiruItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area = scrapy.Field() #南山、龙岗等

    eArea = scrapy.Field() #蛇口等
    
    house = scrapy.Field() #房子名字等

    price = scrapy.Field() #价格等

    unit = scrapy.Field() #单位