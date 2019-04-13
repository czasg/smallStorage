import re


def get_next_page(url, format=None, jump=None, diff="_", step=1, check_current_page=None, **kwargs):
    def next_page(steps):
        if isinstance(steps, str):
            steps = int(steps) + step
            print("当前第%d页" % steps)
            return steps
        elif isinstance(steps, int):
            print("当前第%d页" % steps)
            return steps
    url = _check_current_page(url, format, check_current_page) if check_current_page else url
    if not format:
        # format = "index_%d"
        return url

    if jump is None:
        reRule = format.replace("%d", "(\d+)")
        return re.sub(reRule, lambda v: format % next_page(v.group(1)), url)
    reRule = re.sub(diff + "%d", "(?:" + diff + "(\d+))?", format)
    reRule = "(?!htt)" + reRule  # bug
    # reRule = format.replace(diff + "%d", "(?:" + diff + "(\d+))?")
    return re.sub(reRule, lambda v: format % next_page(v.group(1) or jump), url)

# 或许并不需要，可以删除
def _check_current_page(url, format, check_next_page):
    if re.search(format.replace("%d", "(\d+)?"), url):
        return url
    # try:
    #     check,num = check_next_page.split("-")
    #     return check.join((url, format)) % (int(num)-1)
    # except:
    #     raise ValueError("'-' must in check_next_page, format is char+int")
    return "".join((url, check_next_page))

if __name__ == "__main__":
    url = 'http://sz.ziroom.com/z/nl/z3-d23008679-b612400051.html'
    for i in range(10):
        url = get_next_page(url, format="p=%d", check_next_page="?-3")
        print(url)


    # url = 'www.baidu.com/index_1.html'  # -> index_2
    # print(get_next_page(url, jump=1))
    # url = 'www.baidu.com/index.html'  # -> index_1
    # print(get_next_page(url, jump=2))
    # url = 'www.baidu.com/index.html'
    # print(get_next_page(url, format="index-%d",jump=10, diff="-"))
    # url = 'www.baidu.com/index.html'
    # print(get_next_page(url, format="index_%d"))
    # url = 'www.baidu.com/index.html/p'
    # print(get_next_page(url, format="p_%d", jump=2))
    # url = 'www.baidu.com/index.html'
    # for i in range(10):
    #     url = get_next_page(url, format="index%d", jump=2, diff="")
    #     print(url)
    # url = 'http://sz.ziroom.com/z/nl/z3-d23008679-b612400051.html'
    # print(get_next_page(url, format="p=%d", jump=2, check_next_page="?"))

    # url = 'http://sz.ziroom.com/z/nl/z3-d23008679-b612400051.html'
    # for i in range(10):
    #     url = get_next_page(url, format="p=%d", jump=2, check_next_page="?", diff="=")
    #     print(url)

    # url = 'http://sz.ziroom.com/z/nl/z3-d23008679-b612400051.html'
    # print(get_next_page(url, format="p=%d", check_next_page="?p=1"))

    # url = 'http://sz.ziroom.com/z/nl/z3-d23008679-b612400051.html'
    # for i in range(10):
    #     url = get_next_page(url, format="p=%d",check_current_page="?p=1")
    #     print(url)
