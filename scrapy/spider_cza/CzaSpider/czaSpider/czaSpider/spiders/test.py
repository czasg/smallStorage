from czaSpider.czaBaseSpider import czaSpider
from czaSpider.czaTools import *


class MySpider(czaSpider):
    name = "test-housePrice"
    author = "czaOrz"
    custom_settings = get_custom_settings(name)

    # url = "http://wh.ziroom.com/z/nl/z3.html"
    url = "http://sz.ziroom.com/z/nl/z3-d23008679-b612400051.html?p=1"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'gr_user_id=676447e6-a86f-43d4-8786-0c4d93bf1589; SZ_nlist=%7B%2261492809%22%3A%7B%22id%22%3A%2261492809%22%2C%22sell_price%22%3A1890%2C%22title%22%3A%22%5Cu5357%5Cu5c71%5Cu533a%5Cu6d77%5Cu4e0a%5Cu4e16%5Cu754c2%5Cu53f7%5Cu7ebf%28%5Cu86c7%5Cu53e3%5Cu7ebf%29%5Cu6c34%5Cu6e7e%5Cu6d77%5Cu660c%5Cu5927%5Cu53a63%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1548942593%2C%22usage_area%22%3A10.2%2C%22floor%22%3A%225%22%2C%22floor_total%22%3A%227%22%2C%22room_photo%22%3A%22g2m1%5C%2FM00%5C%2F01%5C%2FDB%5C%2FChAFBlwScmmAY8IRAAkIorBCL_A864.jpg%22%2C%22city_name%22%3A%22%5Cu6df1%5Cu5733%22%7D%7D; __utm_source=pinzhuan; __utm_medium=baidu; ZIROOM_PHONE=9; gr_session_id_8da2730aaedd7628=df0f1a1f-89f2-4add-9c57-14c59dcced65; gr_session_id_8da2730aaedd7628_df0f1a1f-89f2-4add-9c57-14c59dcced65=true; mapType=%20; CURRENT_CITY_CODE=440300; CURRENT_CITY_NAME=%E6%B7%B1%E5%9C%B3',
        'Host': 'sz.ziroom.com',
        'Referer': 'http://sz.ziroom.com/z/nl/z3.html',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    def parse(self, response):
        # print(response.text)
        yield from traverse_urls(response, self, '//div[@class="t_shuaichoose_order"]/following-sibling::ul[@id="houseList"]/li/div[1]/a/@href',
                                 next_page_format="p=%d",check_next_page="?-2")

    # def parse(self, response):
    #     yield from traverse_urls(response, self, '//dl[@class="clearfix zIndex6"]/dd/ul'
    #                                              '/li/div/span[position()>1]/a/@href',
    #                              next_page_format="p=%d",check_next_page="?-2")

    # def parse(self, response):
    #     yield from traverse_urls(response, self, '//dl[@class="clearfix zIndex6"]/dd/ul'
    #                                              '/li/div/span[position()>1]/a/@href',
    #                              callback=self.test)
    #
    # def test(self, response):
    #     yield self.process_item(url=response.url, price=123, place="Wuhan")


if __name__ == "__main__":
    MySpider.cza_run_spider()
    # MySpider.process_item()
    # MySpider.processDataFromDatabase()
    # shutil.rmtree()
