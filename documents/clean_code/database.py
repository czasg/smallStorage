# 望文知义
img_path = img_download(response.urljoin(img))
price_template = img2num(img_path)
img_remove(img_path)

b = img_download(response.urljoin(a))
b = img2num(b)
img_remove(b)

# 避免误导
source = get_source()
so = get_source()
urls = ["http","http"]
us = ["http","http"]

# 有意义的区分
def func(key,value):
    pass
[func(key,value) for key,value in dict.items()]
def func(a1,a2):
    pass
[func(a1,a2) for a1,a2 in dict.items()]

# 可读的名字
def generate_time_about_year_to_second():
    pass
def genymdhms():
    pass

# 可搜索的名字
MONGO_INFO = {"host":"localhost", "port":27017}
mi = {"host":"localhost", "port":27017}

# 类名尽量为名词而非动词,函数名则尽量为动词
class human(object):
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
    def get_height(self):
        return self.height
class MakingThinking(object):
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
    def height(self):
        return self.height

# 只做一件事
def data_from_xpath(response, xpath_rule, first=False, join=False,
                    returnList=False, is_url=False, is_urls=False, **kwargs):
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

# try-except
try:
    doSomething()
except Exception:
    doException()
else:
    doNextThing()
finally:
    done()

# 垂直方向上的间隔
def func1():
    pass

def func2():
    pass

def func3():
    pass

def func1():
    pass
def func2():
    pass
def func3():
    pass

# 垂直方向上的靠近
name = get_name()
age = get_age()

guess_sex(name)
guess_character(age)
guess_height(name, age)


name = get_name()
age = get_age()
guess_sex(name)
guess_character(age)
guess_height(name, age)

# 垂直距离
def func1():
    func2()

def func2():
    func3()

def func3():
    func4()

def func4():
    pass

def func1():
    func2()
def func2():
    func3()
def func3():
    func4()
def func4():
    pass