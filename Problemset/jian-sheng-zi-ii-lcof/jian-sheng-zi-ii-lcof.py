
# @Title: 剪绳子 II (剪绳子 II LCOF)
# @Author: 18015528893
# @Date: 2021-01-07 21:17:47
# @Runtime: 1312 ms
# @Memory: 16 MB

class Solution:
    def cuttingRope(self, n: int) -> int:
        memo = dict()

        def dp(i):
            if i == 2:
                return 1
            if i in memo:
                return memo[i]
            res = 0
            for j in range(2, i):
                res = max(res, max(j * dp(i - j), j * (i - j)))
            memo[i] = res
            return memo[i]
        return dp(n) % 1000000007

