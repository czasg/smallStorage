from czaSpider.czaBaseSpider import czaSpider
from czaSpider.czaTools import *


class MySpider(czaSpider):
    name = "test-housePrice"
    author = "czaOrz"
    collName = get_collection_name(name, timeStr=True)
    dbName = get_database_name(name)
    # custom_settings = get_custom_settings(name)

    # url = "http://wh.ziroom.com/z/nl/z3.html"
    url = "http://sz.ziroom.com/z/nl/z3-d23008679-b612400051.html?p=1"
    # def parse(self, response):
    #     print([response.text[:100]])
    # formdata = {"header"}

    # def parse(self, response):
    #     yield from traverse_urls(response, self, '//div[@class="t_shuaichoose_order"]/following-sibling::ul[@id="houseList"]/li/div[1]/a/@href',
    #                              next_page_format="p=%d",check_next_page="?p=2")

    # def parse(self, response):
    #     yield from traverse_urls(response, self, '//dl[@class="clearfix zIndex6"]/dd/ul'
    #                                                  '/li/div/span[position()>1]/a/@href',
    #                                  callback=self.one)
    # def one(self, response):
    #     item = {"releaseTime":"Today"}
    #     yield from traverse_urls(response, self, '//div[@class="t_shuaichoose_order"]'
    #                                              '/following-sibling::ul[@id="houseList"]/li/div[1]/a/@href',
    #                              next_page_format="p=%d",check_current_page="?p=1",item=item)


    # def parse(self, response):
    #     yield from traverse_urls(response, self, '//div[@class="t_shuaichoose_order"]'
    #                                              '/following-sibling::ul[@id="houseList"]/li/div[1]/a/@href',
    #                              next_page_format="p=%d",check_current_page="?p=1")

    # def parse(self, response):
    #     yield from traverse_urls(response, self, '//dl[@class="clearfix zIndex6"]/dd/ul'
    #                                              '/li/div/span[position()>1]/a/@href',
    #                              url_pipe=lambda url:url+"?p=1",
    #                              callback=self.test)

    # def test(self, response):
    #     yield self.process_item(url=response.url, price=123, place="Wuhan")

    # def test(self, response):
    #     yield from traverse_urls(response, self,'//div[@class="t_shuaichoose_order"]'
    #                                             '/following-sibling::ul[@id="houseList"]'
    #                                             '/li/div[1]/a/@href',
    #                             next_page_format="p=%d")

    def parse(self, response):
        print(response.url)
        yield self.process_item(url=response.url)

if __name__ == "__main__":
    MySpider.cza_run_spider()
    # MySpider.process_item()
    # MySpider.processDataFromDatabase()
    # shutil.rmtree()
