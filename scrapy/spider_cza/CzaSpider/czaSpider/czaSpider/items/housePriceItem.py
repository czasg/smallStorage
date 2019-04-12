from czaSpider.items import czaBaseItem, process_base_item
from czaSpider.czaTools import *


class Item(czaBaseItem):
    # 此处继承父类，并指定需要拓展的类
    price = scrapy.Field()
    place = scrapy.Field()


def housePriceItem(**kwargs):
    item = Item()
    item.update(process_base_item(**kwargs))

    item["price"] = kwargs.pop('price', None)
    item["place"] = kwargs.pop('place', None)

    return item
