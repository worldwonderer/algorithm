from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[n][k][c] 表示第n天，还有k次交易机会，目前状态是持有还是卖出，最多能获得的利润
        # 这道题k = 1
        n = len(prices)
        dp = [[0, 1] for _ in range(n+1)]
        dp[0][0] = 0
        dp[0][1] = float('-inf')
        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])  # 由上一次的卖转移而来
            # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i-1])
            dp[i][1] = max(dp[i-1][1], -prices[i-1])  # 由上一次的买转移而来
        return dp[-1][0]


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([7,1,5,3,6,4])
