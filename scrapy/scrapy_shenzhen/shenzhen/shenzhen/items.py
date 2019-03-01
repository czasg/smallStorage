# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShenzhenItem(scrapy.Item):

    job_salary = scrapy.Field()

    job_site = scrapy.Field()
    
    job_exp = scrapy.Field()

    tag = scrapy.Field()