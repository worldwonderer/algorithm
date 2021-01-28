class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = dict()
        l = len(s)

        def dp(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == s[j]:
                memo[(i, j)] = dp(i + 1, j - 1) + 2
            else:
                memo[(i, j)] = max(dp(i + 1, j), dp(i, j - 1))
            return memo[(i, j)]

        return dp(0, l - 1)
