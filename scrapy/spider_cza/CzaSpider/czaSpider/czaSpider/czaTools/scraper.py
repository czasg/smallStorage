from scrapy import Request


def traverse_urls(response, spider, xpath_ruler=None,
                  callback=None, extend_callbeck=None,
                  **kwargs):
    detail_urls = kwargs.get("detail_urls", None)
    urls = detail_urls if detail_urls else response.xpath(xpath_ruler).extract()
    if not urls:
        raise ValueError("what you get urls is None, Please check it's correctness")
    for pipe in kwargs.get("url_pipe", []):
        urls = [pipe(url) for url in urls]

    for url in urls:
        if extend_callbeck:
            yield extend_callbeck(url)
        elif callback:
            yield Request(url, callback)
        else:
            raise ValueError("Please appoint the callback func")
    pass