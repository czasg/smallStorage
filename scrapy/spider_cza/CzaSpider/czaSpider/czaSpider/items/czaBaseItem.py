from czaSpider.czaTools import *


class czaBaseItem(scrapy.Item):
    spiderName = scrapy.Field()

    author = scrapy.Field()

    url = scrapy.Field()

    releaseTime = scrapy.Field()

    more = scrapy.Field()
