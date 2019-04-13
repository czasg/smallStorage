from scrapy import Request

from .url_func import get_next_page


def traverse_urls(response, spider, xpath_rule=None, next_page_format=None,
                  allow_next_page=True,
                  callback=None, extend_callback=None,
                  **kwargs):
    detail_urls = kwargs.get("detail_urls", None)
    urls = detail_urls if detail_urls else data_from_xpath(response, xpath_rule, is_urls=True)
    # if not urls:
    #     raise ValueError("what you get urls is None, Please check it's correctness")
    url_pipe = kwargs.get("url_pipe", None)
    urls = [url_pipe(url) for url in urls] if url_pipe else urls
    for pipe in kwargs.get("url_pipes", []):
        urls = [pipe(url) for url in urls]

    for url in urls:
        if extend_callback:
            yield extend_callback(url)
        elif callback:
            yield Request(url, callback)
        else:
            yield spider.process_item(url=url, )
    # 未做去重，增量是个大问题
    if allow_next_page and urls:
        # print(response.url, next_page_format, kwargs)
        # print(get_next_page(response.url, next_page_format, **kwargs), '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        yield Request(get_next_page(response.url, next_page_format, **kwargs), response.request.callback)


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


def data_from_xpath(response, xpath_rule, join=False, returnList=False, is_url=False, is_urls=False, **kwargs):
    if join:
        return xpathJ(response, xpath_rule, **kwargs)
    elif returnList:
        return response.xpath(xpath_rule).extract()
    elif is_url:
        url = xpathF(response, xpath_rule)
        return response.urljoin(url) if url else None
    elif is_urls:
        urls = response.xpath(xpath_rule).extract()
        return [response.urljoin(each) for each in urls if each]
    else:
        return xpathF(response, xpath_rule)
