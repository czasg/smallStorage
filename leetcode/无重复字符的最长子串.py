"""
思路，计算出不重复的字符串，首先要找到每一个重复的点，找到后需要读取其下标
故使用dict保存一个子串的下标，然后重复后就立即取出此下标
而且下标使用最大的一个重复字串的下标，代表着一旦重复后从此开始在此进行计算
"""

class Test(object):
    @classmethod
    def solution1(cls, s):
        dict = {}
        flag, res = 0, 0
        for index, value in enumerate(s):
            if value in dict:
                flag = max(flag, dict[value])
            res = max(res, index - flag + 1)
            dict[value] = index + 1
        return res


testSet = {"s1": "chenziang", "res": 7}
