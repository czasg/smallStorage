class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        res1 = string[1:] if '-' in string else string
        res = int('-' + res1[::-1]) if '-' in string else int(res1[::-1])
        return res if -2147483648 < res < 2147483647 else 0
