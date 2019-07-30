class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = []
        for g in zip(*strs):
            if len(set(g)) == 1:
                res.append(g)
            else:
                break
        return strs[0][:len(res)] if strs else ''

"""
这题用zip和set的特性来解，简直了，牛逼
"""
