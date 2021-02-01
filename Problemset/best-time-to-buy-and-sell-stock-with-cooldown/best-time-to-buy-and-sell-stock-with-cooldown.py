
# @Title: 最佳买卖股票时机含冷冻期 (Best Time to Buy and Sell Stock with Cooldown)
# @Author: 18015528893
# @Date: 2021-02-01 23:24:09
# @Runtime: 48 ms
# @Memory: 15.1 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 1] for _ in range(n+1)]
        for i in range(1, n+1):
            if i == 1:
                dp[i-1][0] = 0
                dp[i-1][1] = float('-inf')
            if i == 2:
                dp[i-2][0] = 0 
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i-1])
        return dp[-1][0]

