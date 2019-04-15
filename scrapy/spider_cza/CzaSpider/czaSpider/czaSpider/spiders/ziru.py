from czaSpider.czaBaseSpider import czaSpider
from czaSpider.czaTools import *


class MySpider(czaSpider):
    name = "ziru-housePrice"
    author = "czaOrz"
    collName = get_collection_name(name, timeStr=True)
    dbName = get_database_name(name)
    custom_settings = get_custom_settings(name)

    url = "http://wh.ziroom.com/z/nl/z3.html"

    def parse(self, response):
        city = data_from_xpath(response, '//span[@id="curCityName"]/text()', first=True)
        places = data_from_xpath(response, '//dl[@class="clearfix zIndex6"]'
                                           '/dd/ul/li/div/span[position()>1]')
        for place in places:
            area_place = data_from_xpath(place, './../preceding-sibling::span/a/text()', first=True)
            son_place = data_from_xpath(place, './a/text()', first=True)
            house_place = "-".join((city, area_place, son_place))

            url = data_from_xpath(place, './a/@href', is_url=True, source=response)
            yield from traverse_urls(response, self, detail_urls=url,
                                     extend_callback= \
                                         lambda url: Request(url, self.process, meta={"house_place": house_place}))

    def process(self, response):
        house_place = response.meta["house_place"]
        self.item.setdefault("house_place", house_place)
        try:
            img, price_list = re.search('"image":"(.*?)".+offset":(\[.*?\])};', response.text).groups()
        except AttributeError:
            return
        price_list = eval(price_list)

        img_path = img_download(response.urljoin(img))
        price_template = img2num(img_path)
        img_remove(img_path)

        houses = data_from_xpath(response, '//div[@class="t_shuaichoose_order"]'
                                           '/following-sibling::ul[@id="houseList"]/li')
        item, items = {}, {}
        urls = []
        item["house_place"] = house_place
        for index, house in enumerate(houses):
            price = [price_template[i] for i in price_list[index]]
            item["house_price"] = int("".join([str(v) for v in price]))

            item["house_name"] = data_from_xpath(house, './/a[@class="t1"]/text()', first=True)

            item["house_area"], \
            item["house_floor"], \
            item["house_scale"], \
            item["distance_from_subway"] = \
                data_from_xpath(house, './/div[@class="detail"]/p/span/text()', returnList=True)

            url = data_from_xpath(house, './/a[@class="t1"]/@href', is_url=True, source=response)
            urls.append(url)
            items.setdefault(url, item)
        yield from traverse_urls(response, self, detail_urls=urls, meta=response.meta,
                                 items=items, next_page_format="p=%d",
                                 check_current_page="?p=1",next_page_without_new_urls=True)

if __name__ == "__main__":
    MySpider.cza_run_spider()
    # todo 定时器模块
    # while True:
    #     while True:
    #         now = datetime.datetime.now()
    #         if now.minute == 40:
    #             break
    #         print("waiting for time to execute code")
    #         time.sleep(60)
    #     MySpider.cza_run_spider()