class Test(object):
    @classmethod
    def solution1(cls, s: str) -> str:
        res = s[0] if s else s
        dict = {}
        for index, value in enumerate(s):
            if value in dict:
                dict[value].append(index)
                for val in dict[value]:
                    aim = s[val: index + 1]
                    reAim = aim[::-1]
                    if aim == reAim and len(aim) >= len(res):
                        res = aim
                        break
            dict.setdefault(value, [index])
        return res

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

    @classmethod
    def solution4(cls, s: str) -> str:
        res = s[0] if s else s
        dict = {}
        for index, value in enumerate(s):
            if value in dict:
                dict[value].append(index)
                print('111',value,dict[value])
                for val in dict[value]:
                    string = s[val: index + 1]
                    reString = string[::-1]
                    if string == reString and len(string) >= len(res):
                        print(string, val, index + 1)
                        res = string
                        break
            dict.setdefault(value, [index])
            print(dict)
        return res

testSet = {"str":"adacada", "res":"adacada"}

if __name__ == "__main__":
    # res = "babadada"
    # res = "adacada"
    # res = 'a'
    res = 'ac'
    print(Test.solution1(res))
