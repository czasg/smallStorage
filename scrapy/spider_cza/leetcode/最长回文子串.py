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
            print(dict)
        return s[left:right + 1]

    @classmethod
    def solution2(cls, s: str) -> str:
        if not s:
            return ""
        lon, res = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    if len(s[i:j + 1]) >= lon:
                        lon = len(s[i:j + 1])
                        res = s[i:j + 1]
        return res

    @classmethod
    def solution3(cls, s: str) -> str:
        def judgeStr(x):
            return x == x[::-1]

        dict = {}
        flag, res = 0, 0
        l, r, left, right = 0, 0, 0, 0
        for index, value in enumerate(s):
            if value in dict:
                dict[value].append(index)
                for i, v in enumerate(dict[value]):
                    for j in range(i, len(dict[value])):
                        if judgeStr(s[dict[value][i]:dict[value][j] + 1]):
                            l, r = dict[value][i], dict[value][j]
                            if (r - l) >= res:
                                res = r - l
                                left, right = l, r
            dict.setdefault(value, [index])
        return s[left:right + 1]


if __name__ == "__main__":
    res = "babadada"
    # res = "adacada"
    print(Test.solution1(res))
