
# @Title: 正则表达式匹配 (Regular Expression Matching)
# @Author: 18015528893
# @Date: 2021-02-18 14:22:26
# @Runtime: 40 ms
# @Memory: 15.3 MB

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        memo = dict()

        def dp(i, j):
            if j == n:
                return i == m
            if i == m:
                if len(p[j:]) % 2 == 1:
                    return False
                else:
                    while j+1 < n:
                        if p[j+1] != '*':
                            return False
                        j += 2
                    return True

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == p[j] or p[j] == '.':
                if j+1 < n and p[j+1] == '*':
                    res = dp(i+1, j) or dp(i, j+2)
                else:
                    res = dp(i+1, j+1)
            else:
                if j+1 < n and p[j+1] == '*':
                    res = dp(i, j+2)
                else:
                    res = False

            memo[(i, j)] = res
            return res

        return dp(0, 0)


