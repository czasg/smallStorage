# from czaSpider.czaTools import *

class CzaSpiderPipeline(object):
    def process_item(self, item, spider):
        res = dict(item.copy())
        try:
            spider.collection.insert_one(res)
        except:
            raise ValueError("insert error")
        else:
            print("insert done")
        finally:
            return item

