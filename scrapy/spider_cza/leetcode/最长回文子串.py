class Test(object):
    @classmethod
    def solution1(cls, s):
        dict = {}
        l, r = 0, 0
        flag, res, left, right = 0, 0, 0, 0
        for index, value in enumerate(s):
            if value in dict:
                flag = dict[value]
                left, right = flag, index
                print(left, right)
            # res = max(res, right-left)
            if res < right - left:
                res = right - left
                l, r = left, right
            # dict[value] = index
            dict.setdefault(value, index)
        print(l, r)
        return s[l:r + 1]