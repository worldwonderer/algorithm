
# @Title: 最小覆盖子串 (Minimum Window Substring)
# @Author: 18015528893
# @Date: 2021-02-28 12:15:20
# @Runtime: 188 ms
# @Memory: 15.3 MB

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for char in t:
            need[char] += 1
        
        window = defaultdict(int)
        left = right = 0
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
            
            print(left, right, valid)

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
