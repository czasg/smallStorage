# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZlzpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    name = scrapy.Field()

    place = scrapy.Field()

    salary = scrapy.Field()

    child_id = scrapy.Field()

    type_s = scrapy.Field()