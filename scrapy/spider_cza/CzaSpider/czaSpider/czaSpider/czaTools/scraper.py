from scrapy import Request

from .url_func import get_next_page


def traverse_urls(response, spider, xpath_rule=None, next_page_format=None, next_page_without_new_urls=False,
                  allow_next_page=True, meta=None,callback=None, extend_callback=None,
                  **kwargs):
    """
    遍历url，封装了翻页逻辑
    :param response:
    :param spider:
    :param xpath_rule: xpath规则
    :param next_page_format: 翻页的样式，如"index_%d"、"p=%d"。有去重逻辑，无新url则不会翻页
    :param next_page_without_new_urls: 当不存在新url时，可以翻页
    :param allow_next_page: 允许翻页
    :param meta:
    :param callback: 回调函数
    :param extend_callback: 其他的回调，可以指定form请求
    :param kwargs:
    :return:
    """
    detail_urls = kwargs.get("detail_urls", None)
    urls = detail_urls if detail_urls else data_from_xpath(response, xpath_rule, is_urls=True)
    urls = urls if isinstance(urls, list) else [urls]
    url_pipe = kwargs.get("url_pipe", None)
    urls = [url_pipe(url) for url in urls] if url_pipe else urls
    for pipe in kwargs.get("url_pipes", []):
        urls = [pipe(url) for url in urls]

    # 去重
    new_urls = [url for url in urls if not spider.collection.count({"url": url})]
    print("共%d条其中%d条未爬" % (len(urls), len(new_urls)))
    for url in new_urls:
        if not url:
            continue
        if extend_callback:
            yield extend_callback(url)
        elif callback:
            yield Request(url, callback, meta=meta)
        else:
            item = kwargs.get("items", {})
            if item:
                item = item.get(url, {})
            if isinstance(item, dict):
                item.setdefault("url", url)
                yield spider.process_item(**item)
            else:
                raise Exception("parameter items must be an dict")
    # 未做去重，增量是个大问题
    if allow_next_page and new_urls or (urls and next_page_without_new_urls):
        yield Request(get_next_page(response.url, next_page_format, **kwargs), response.request.callback, meta=meta)


def xpathF(response, xpath_rule):
    return response.xpath(xpath_rule).extract_first()


def xpathJ(response, xpath_rule, sep="", stripEach=True, stripEnd=True):
    """
    使用extract获取list，并根据参数join合并
    :param response: --
    :param xpath_ruler: 数据获取的xpath规则
    :param sep: 合并时join使用的参数，默认为""
    :param stripEach: 是否对每一行执行strip
    :param stripEnd: 是否对结果执行strip
    :return:
    """
    list = response.xpath(xpath_rule).extract()
    if stripEach:
        list = [row.strip() for row in list]
        return sep.join(list)
    res = sep.join(list)
    return res.strip() if stripEnd else res


def data_from_xpath(response, xpath_rule, first=False, join=False,
                    returnList=False, is_url=False, is_urls=False, **kwargs):
    """
    从xpath中获取数据，（封装extract()、extract_first()、response.urljoin()）
    :param response: scrapy的response数据结构 or Select数据结构，若为后者，请附带参数"source=response"指定源
    :param xpath_rule: xpath获取规则
    :param first: 请参考学长你自己写的xpath()功能
    :param join: 请参考学长你自己写的jxpath()功能
    :param returnList: extract()返回列表，参考response.xpath(xpath_rule).extract()
    :param is_url: 获取xpath中单个url并返回response.urljoin()清洗结果，
                    参考response.urljoin(response.xpath(xpath_rule).extract_first())
    :param is_urls: 获取xpath中多个urls，并返回response.urljoin()清洗结果，
                    参考[response.urljoin(url) for url in urls]，其中urls为extract()的结果
    :param kwargs: 可指定源response，source=response
    :return:
    """
    if first:
        return xpathF(response, xpath_rule)
    elif join:
        return xpathJ(response, xpath_rule, **kwargs)
    elif returnList:
        return response.xpath(xpath_rule).extract()
    elif is_url:
        url = xpathF(response, xpath_rule)
        response = kwargs.get("source", response)
        return response.urljoin(url) if url else None
    elif is_urls:
        urls = response.xpath(xpath_rule).extract()
        response = kwargs.get("source", response)
        return [response.urljoin(each) for each in urls if each]
    else:
        return response.xpath(xpath_rule)
