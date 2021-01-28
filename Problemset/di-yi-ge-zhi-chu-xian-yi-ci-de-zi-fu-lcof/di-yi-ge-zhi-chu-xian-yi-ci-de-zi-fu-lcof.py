
# @Title: 第一个只出现一次的字符 (第一个只出现一次的字符  LCOF)
# @Author: 18015528893
# @Date: 2021-01-26 17:20:01
# @Runtime: 168 ms
# @Memory: 15.1 MB

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        for char in s:
            if d[char] == 1:
                return char
        return " "

