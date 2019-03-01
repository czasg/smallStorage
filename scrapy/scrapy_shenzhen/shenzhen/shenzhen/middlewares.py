# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from .settings import USER_AGENT

class ShenzhenSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ShenzhenDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        #print('##################################')
        headers = {
            #'Content-Length':str(len(data))
            'Accept': 'application/json, text/plain, */*',
            #'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'adfbid2=0; sts_deviceid=167b73ceebb559-08d911295dfe95-424e0b28-1049088-167b73ceebc536; adfbid=0; ZP_OLD_FLAG=false; dywec=95841923; sts_sg=1; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C05x-60KqiAs0q0bIT00000Ftg0dC00000UlSnO1.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15yc1nhn1njN-nj0snHDvrHm0IHd7nDfznbD3PDnkPjDzwRmkwjDsrDDkrDmzn104PWFjwfK95gTqFhdWpyfqn1DLn1TvP1bznBusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1Y1njfsns%26tpl%3Dtpl_11535_18778_14772%26l%3D1510152095%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3173767922_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D147%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D2242; __utmc=269921210; _jzqc=1; _jzqy=1.1544967483.1548157509.1.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.-; _jzqckmp=1; __xsptplus30=30.3.1548157546.1548157546.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23qYFnne5Y6cxG_yKLYsiz9CGRCJcKGBwb%23; jobRiskWarning=true; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1548157509,1548157546,1548157570; LastCity=%E6%B7%B1%E5%9C%B3; LastCity%5Fid=765; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22695062284%22%2C%22%24device_id%22%3A%22167b73cf8ec91-01fe862c477b55-424e0b28-1049088-167b73cf8ed324%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%22167b73cf8ec91-01fe862c477b55-424e0b28-1049088-167b73cf8ed324%22%7D; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; acw_tc=3ccdc16215481596502866644e4d182c0bb8d7f8bdbc23054788402497bb3c; sts_sid=16875bc90a5aa9-08d77fe78180cf-424e0b28-1049088-16875bc90a6524; dywea=95841923.597616740870499700.1544967483.1548157509.1548165087.3; dywez=95841923.1548165087.3.4.dywecsr=sou.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; __utma=269921210.1792001410.1544967483.1548157570.1548165087.4; __utmz=269921210.1548165087.4.4.utmcsr=sou.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.2975923148704632000.1544967483.1548157509.1548165087.3; _jzqx=1.1548165087.1548165087.1.jzqsr=sou%2Ezhaopin%2Ecom|jzqct=/.-; JsNewlogin=2085186854; JSloginnamecookie=15607173521; JSShowname=%E9%99%88%E5%AD%90%E6%98%82; at=8c98eedd09f64cc5a27fffdf2afa45d6; Token=8c98eedd09f64cc5a27fffdf2afa45d6; rt=ee14f32a1ac04dc9a24f74c29d13793e; JSpUserInfo=386b2e695671416556700069456d5d6a5b6b43775d6f44355275216b2469567146655a700369456d5c6a586b4677566f45355b755c6b51693e71396552707dff2536690c526b3477286f4d3550755a6b58695e7143655d700369406d5e6a296b0077146f5e350a75026b0769507124653b700869446d506a286b2577586f403544755f6b4a695971466555700069446d506a286b3d77586f41355275386b2b6956713d6522700c69406d5b6a5f6b4377576f48355d755f6b51693e712365527004694e6d386a206b4c77556f4b359; uiioit=3b622a6459640e644e64426a586e546e566456385c77507751682c622a64596408644c646; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1548166344; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22ccdc1ebb-68f4-4c50-9bee-f1c32e55c4d0-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22//jobs%22:{%22actionid%22:%2270cbdb65-cc5d-4ee2-86ea-2733cf531219-jobs%22%2C%22funczone%22:%22dtl_best_for_you%22}}; sts_evtseq=24',
            'Host': 'fe-api.zhaopin.com',
            'Origin': 'https://sou.zhaopin.com',
            'Referer': 'https://sou.zhaopin.com/?jl=765&sf=0&st=0&kw=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&kt=3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        useragent = USER_AGENT
        request.headers.setdefault('User-Agent', useragent)
        
        return None
        #return response

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
