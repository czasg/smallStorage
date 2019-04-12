from czaSpider.items import czaBaseItem
from czaSpider.czaTools import *


class Item(czaBaseItem):
    # 此处继承父类，并指定需要拓展的类
    price = scrapy.Field()
    place = scrapy.Field()


def housePriceItem(**kwargs):
    item = Item()
    item["spiderName"] = kwargs.pop('spiderName', None)
    item["author"] = kwargs.pop('author', "czaOrz")
    item["url"] = kwargs.pop('url', None)
    item["releaseTime"] = kwargs.pop('releaseTime', None)
    item["more"] = kwargs.pop('more', None)

    item["price"] = kwargs.pop('price', None)
    item["place"] = kwargs.pop('place', None)

    return item
