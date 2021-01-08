class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[True] * n for _ in range(n)]
        res = s[0]
        for length in range(1, n):
            for left in range(n):
                right = left + length
                if right >= n:
                    break
                elif length == 1:
                    dp[left][right] = (s[left] == s[right])
                else:
                    dp[left][right] = dp[left + 1][right - 1] and (s[left] == s[right])
                if dp[left][right] and length + 1 > len(res):
                    res = s[left: right + 1]
        return res
