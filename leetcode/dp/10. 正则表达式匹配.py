class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = dict()

        def dp(i, j):
            if j == n:
                return i == m
            if i == m:
                if (n - j) % 2 == 1:
                    return False
                while j + 1 < n:
                    if p[j+1] != "*":
                        return False
                    j += 2
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            res = False

            if s[i] == p[j] or p[j] == '.':
                if j + 1 < n and p[j+1] == '*':
                    res = dp(i, j+2) or dp(i+1, j)
                else:
                    res = dp(i+1, j+1)
            else:
                if j + 1 < n and p[j+1] == '*':
                    res = dp(i, j+2)
                else:
                    res = False

            memo[(i, j)] = res
            return res

        return dp(0, 0)
