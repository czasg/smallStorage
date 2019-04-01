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
        yield self.process_item(url=response.url)


if __name__ == "__main__":
    MySpider.cza_run_spider()
