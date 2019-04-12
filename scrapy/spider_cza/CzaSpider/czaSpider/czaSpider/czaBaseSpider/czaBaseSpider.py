import logging

from czaSpider.czaTools import *
from czaSpider import items

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class czaSpider(scrapy.Spider):
    name = "czaSpider"
    author = "czaOrz"

    def start_requests(self):
        log.info("spider start...")
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
        kwargs.setdefault("spiderName",cls.name)
        kwargs.setdefault("author", cls.author)
        itemName = cls.name[cls.name.rfind('-') + 1:] + "Item"
        return getattr(items, itemName)(**kwargs)

    @classmethod
    def cza_run_spider(cls):
        if cls.author == "czaOrz":
            os.system("scrapy crawl {}".format(cls.name))
        else:
            log.error("auther is not czaOrz, Who are you?")
            sys.exit(0)

    @classmethod
    def processDataFromDatabase(cls):
        pass