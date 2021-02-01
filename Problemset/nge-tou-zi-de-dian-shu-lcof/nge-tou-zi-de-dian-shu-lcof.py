
# @Title: n个骰子的点数 (n个骰子的点数  LCOF)
# @Author: 18015528893
# @Date: 2021-02-01 19:07:10
# @Runtime: 36 ms
# @Memory: 15.1 MB

class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        # dp[n][s]表示投第n个骰子时，点数和为s的次数
        dp = [[0] * (6*n+1) for _ in range(1, 67)]
        for i in range(1, 7):
            dp[1][i] = 1

        for i in range(2, n+1):
            for j in range(i, i*6+1):
                for k in range(1, 7):
                    dp[i][j] += dp[i-1][j-k]

        res = []
        for i in range(n, n*6+1):
            res.append(dp[n][i]*1./6**n)
        return res

