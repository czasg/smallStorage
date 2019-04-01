# from czaSpider.czaTools import *

class CzaSpiderPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item