import re
"""
正则：'(^[\-\+]?\d+)'
这个[0:1]，get到了。不需要用if判断
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('(^[\+\-]?\d+)', s.strip())[0:1] or '0'), 2**31 - 1), -2**31)