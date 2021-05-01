
# @Title: 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
# @Author: 18015528893
# @Date: 2021-02-17 18:22:13
# @Runtime: 80 ms
# @Memory: 14.9 MB

from collections import defaultdict 


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = right = 0
        max_length = 0
        window = defaultdict(int)
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1

            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
        
            max_length = max(right-left, max_length)
        return max_length

