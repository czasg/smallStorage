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
        urls = ["http://www.kk44kk.com","http://www.ye321.com"]
        yield from traverse_urls(response, self, detail_urls=urls,callback=self.test)
        # yield self.process_item(url=response.url)
    def test(self, response):
        print("hello cza's world")

if __name__ == "__main__":
    MySpider.cza_run_spider()
    # MySpider.processDataFromDatabase()
    # shutil.rmtree()
