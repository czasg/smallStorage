import os, sys, re
from functools import reduce

def setting_plus(*settings):
    def add(setting1, setting2): # this is a func to fuse the dict, add all to the setting1
        new_setting = setting1.copy()  # 保留一份新的字典，以
        for s in setting2: # traverse the setting2 as s
            if s not in setting1: # if it is a key and not in setting1, go here
                new_setting[s] = setting2[s] # find different element from setting2, and add them to new_setting?
            elif isinstance(setting2[s], dict): # if the value is dict, recursive the func add
                new_setting[s] = add(setting1[s], setting2[s])
            elif setting2[s] == setting1[s]:
                pass
            else:
                raise ValueError("非字典类型的同名setting不能合并 %s" % str(s))
        return new_setting

    return reduce(add, settings)  # return reduce(add, setting) # 太牛逼了！

class FakeReSearch(object):
    def __init__(self, reRuler):
        self.count = reRuler.count('(') - reRuler.count('(?:')
    def group(self, index):
        assert self.count > index, 'no such group'
        return None
    def groups(self):
        return tuple([None for _ in range(self.count)])
def search(*args):
    return re.search(*args) or FakeReSearch(args[0])

if __name__ == '__main__':
    # path = sys.path
    # print(path)
    # print(path[0])  # 其实path[0]就是运行这个python代码的路径，但是不包括这个运行py文件的名字哦
    # print(os.path.isdir(path[0]))
    # print(os.path.dirname(__file__), __file__)  # __file__是这个文件的完整路径
    # print(os.sep.join(['cza', 'is', 'sg']))

    # dict1,dict2,dict3 = {'1':notebook,'2':22,'3':33},{'4':44,'5':{"22":22}},{'5':{'2':"notebook"}}
    # print(setting_plus(dict1,dict2,dict3))

    a,b = search(r'cza(\d)is(\s)sg', 'cza1is2sg').groups()
    print(a,b)

