
# @Title: 最长公共子序列 (Longest Common Subsequence)
# @Author: 18015528893
# @Date: 2021-01-06 00:09:34
# @Runtime: 1016 ms
# @Memory: 138.1 MB

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                memo[(i, j)] = dp(i - 1, j - 1) + 1
            else:
                memo[(i, j)] = max(dp(i - 1, j), dp(i, j - 1))
            return memo[(i, j)]
        return dp(len(text1) - 1, len(text2) - 1)

