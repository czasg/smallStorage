class Test(object):
    @classmethod
    def solution1(cls, s):
        dict = {}
        res = 0
        for index, value in enumerate(s):
            con = dict.get(value, None)
            if con:
                res = max(res, index - con)
            dict[value] = index
        return res


testSet = {"s1": "chenziang", "res": 4}
