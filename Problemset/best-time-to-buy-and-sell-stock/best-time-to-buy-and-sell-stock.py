
# @Title: 买卖股票的最佳时机 (Best Time to Buy and Sell Stock)
# @Author: 18015528893
# @Date: 2021-02-01 22:11:17
# @Runtime: 792 ms
# @Memory: 29.5 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 1] for _ in range(n+1)]
        dp[0][0] = 0
        dp[0][1] = float('-inf')
        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1], -prices[i-1])
        return dp[-1][0]

