
# @Title: 零钱兑换 (Coin Change)
# @Author: 18015528893
# @Date: 2020-12-25 22:02:05
# @Runtime: 1336 ms
# @Memory: 14.9 MB

from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = dict()
        # def dp(memo, n):
        #     if n in memo:
        #         return memo[n]
        #     if n == 0:
        #         return 0
        #     if n < 0:
        #         return -1
        #     res = float('INF')
        #     for coin in coins:
        #         subproblem = dp(memo, n-coin)
        #         if subproblem == -1:
        #             continue
        #         res = min(res, 1+subproblem)
        #     memo[n] = res if res != float('INF') else -1
        #     return memo[n]
        # return dp(memo, amount)
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(0, len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])
        return -1 if dp[amount] == amount+1 else dp[amount]

