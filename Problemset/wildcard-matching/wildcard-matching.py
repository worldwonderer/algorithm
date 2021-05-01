
# @Title: 通配符匹配 (Wildcard Matching)
# @Author: 18015528893
# @Date: 2021-02-22 14:16:35
# @Runtime: 688 ms
# @Memory: 128.8 MB

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        memo = dict()

        def dp(i, j):
            if j == n:
                return i == m
            if i == m:
                while j < n:
                    if p[j] != '*':
                        return False
                    j += 1
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            res = False
            if s[i] == p[j] or p[j] == '?':
                res = dp(i+1, j+1)
            elif p[j] == '*':
                res = dp(i+1, j) or dp(i, j+1)

            memo[(i, j)] = res
            return res

        return dp(0, 0)


