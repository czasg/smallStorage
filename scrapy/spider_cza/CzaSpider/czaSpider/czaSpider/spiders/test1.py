from czaSpider.czaBaseSpider import czaSpider
from czaSpider.czaTools import *


class MySpider(czaSpider):
    url = "http://sthjj.taian.gov.cn/art/2016/10/13/art_46686_5015303.html"

    def parse(self, response):
        table = data_from_xpath(response, '//div[@class="m-newscontent"]//table')

        all_tr = TableParser.from_html(table).strip().zip()
        print(all_tr)


if __name__ == "__main__":
    MySpider.cza_run_spider()
