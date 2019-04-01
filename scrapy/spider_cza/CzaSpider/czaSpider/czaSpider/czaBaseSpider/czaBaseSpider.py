import logging

from czaSpider.czaTools import *
from czaSpider import items

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class czaSpider(scrapy.Spider):
    name = "czaSpider"
    author = "czaOrz"

    def start_requests(self):
        logger.info("spider start...")
        if hasattr(self, "cza_start_request"):
            yield from self.cza_start_request()
            return
        if hasattr(self, "url"):
            url = self.url
            if url:
                yield Request(url, self.parse)
            else:
                raise ValueError("Please input a effective url")
        else:
            raise ValueError("Please define a url for spider, like url=xxx")

    @classmethod
    def process_item(cls, **kwargs):
        itemName = cls.name[cls.name.rfind('-') + 1:] + "Item"
        return getattr(items, itemName)(**kwargs)

    @classmethod
    def cza_run_spider(cls):
        if cls.author == "czaOrz":
            os.system("scrapy crawl {}".format(cls.name))
        else:
            sys.exit(0)
