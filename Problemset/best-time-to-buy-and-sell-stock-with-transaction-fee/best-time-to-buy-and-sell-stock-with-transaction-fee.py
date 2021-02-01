
# @Title: 买卖股票的最佳时机含手续费 (Best Time to Buy and Sell Stock with Transaction Fee)
# @Author: 18015528893
# @Date: 2021-02-01 23:27:38
# @Runtime: 1004 ms
# @Memory: 24 MB

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, 1] for _ in range(n+1)]
        for i in range(1, n+1):
            if i == 1:
                dp[i-1][0] = 0
                dp[i-1][1] = float('-inf')
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i-1]-fee)
        return dp[-1][0]

