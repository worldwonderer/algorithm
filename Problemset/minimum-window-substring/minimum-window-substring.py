
# @Title: 最小覆盖子串 (Minimum Window Substring)
# @Author: 18015528893
# @Date: 2021-01-29 16:39:06
# @Runtime: 104 ms
# @Memory: 15.1 MB

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        window = defaultdict(int)
        for char in t:
            need[char] += 1

        left = 0
        right = 0
        valid = 0

        start = 0
        length = float('inf')
        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < length:
                    length = right - left
                    start = left

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return '' if length == float('inf') else s[start:start+length]


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))


