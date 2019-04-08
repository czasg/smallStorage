class Test(object):
    @classmethod
    def solution1(cls, s: str) -> str:
        def judgeStr(x):
            return x == x[::-1]

        dict = {}
        flag, res = 0, 0
        l, r, left, right = 0, 0, 0, 0
        for index, value in enumerate(s):
            if value in dict:
                flag = dict[value]
                if judgeStr(s[flag:index + 1]):
                    l, r = flag, index
                # print('l,r', l, r)
            if (r - l) >= res:
                res = r - l
                left, right = l, r
                # print('left, right', left, right)
            dict.setdefault(value, index)
        return s[left:right + 1]

    def func(self, s: str) -> str:
        pass


if __name__ == "__main__":
    res = "babadada"
    print(Test.solution1(res))
