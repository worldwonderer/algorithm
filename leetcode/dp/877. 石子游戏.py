from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = dict()
        n = len(piles)

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == j:
                return piles[i], 0
            left = dp(i + 1, j)[1] + piles[i]
            right = dp(i, j - 1)[1] + piles[j]
            if left > right:
                memo[(i, j)] = (left, dp(i + 1, j)[0])
            else:
                memo[(i, j)] = (right, dp(i, j - 1)[0])
            return memo[(i, j)]

        a, b = dp(0, n - 1)
        return a > b
