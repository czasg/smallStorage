from czaSpider.czaBaseSpider import czaSpider
from czaSpider.czaTools import *


class MySpider(czaSpider):
    name = "test-housePrice"
    author = "czaOrz"
    custom_settings = get_custom_settings(name)

    def cza_start_request(self):
        url = "http://www.baidu.com"
        yield Request(url, self.parse)

    def parse(self, response):
        urls = ["http://www.scrapyd.cn/"]
        # yield self.process_item(url=response.url, price=123, place="Wuhan")
        yield from traverse_urls(response, self, detail_urls=urls,callback=self.test)

    def test(self, response):
        print("hello cza's world")
        yield self.process_item(url=response.url,price=123,place="Wuhan")


if __name__ == "__main__":
    MySpider.cza_run_spider()
    # MySpider.process_item()
    # MySpider.processDataFromDatabase()
    # shutil.rmtree()
