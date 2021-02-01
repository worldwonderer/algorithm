
# @Title: 买卖股票的最佳时机 IV (Best Time to Buy and Sell Stock IV)
# @Author: 18015528893
# @Date: 2021-02-01 23:13:13
# @Runtime: 160 ms
# @Memory: 24.5 MB

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = dp = [ [[0, 1] for _ in range(k+1)]  for _ in range(n+1)]
        for i in range(1, n+1):
            for k in range(1, k+1):
                # base case
                if i == 1:
                    dp[i-1][k][0] = 0
                    dp[i-1][k][1] = float('-inf')
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i-1])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i-1])
        return dp[-1][-1][0]

