
# @Title: 礼物的最大价值 (礼物的最大价值 LCOF)
# @Author: 18015528893
# @Date: 2021-01-25 20:42:10
# @Runtime: 88 ms
# @Memory: 20.3 MB

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            left, up = 0, 0
            if j-1 >= 0:
                left = dp(i, j-1)
            if i-1 >= 0:
                up = dp(i-1, j)
            memo[(i, j)] = max(left, up) + grid[i][j]
            return memo[(i, j)]
        return dp(len(grid)-1, len(grid[0])-1)


