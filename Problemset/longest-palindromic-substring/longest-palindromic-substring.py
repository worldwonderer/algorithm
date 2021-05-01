
# @Title: 最长回文子串 (Longest Palindromic Substring)
# @Author: 18015528893
# @Date: 2021-02-18 14:28:08
# @Runtime: 1000 ms
# @Memory: 15 MB

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        def expand(l, r):
            while l < r:
                if l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            return s[l+1:r]


        ans = ''
        for i in range(len(s)):
            # 奇数
            l = i - 1
            r = i + 1
            k = expand(l, r)
            if len(k) > len(ans):
                ans = k

            # 偶数
            l = i - 1
            r = i + 1 - 1
            k = expand(l, r)
            if len(k) > len(ans):
                ans = k
        return ans


