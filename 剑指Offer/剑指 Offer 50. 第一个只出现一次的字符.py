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
