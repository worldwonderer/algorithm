
# @Title: 最小路径和 (Minimum Path Sum)
# @Author: 18015528893
# @Date: 2021-02-23 22:22:16
# @Runtime: 72 ms
# @Memory: 20.1 MB

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0:
                return float('inf')
            if j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[0][0]
            
            res = min(dp(i-1, j), dp(i, j-1)) + grid[i][j]
            memo[(i, j)] = res
            return res
        
        return dp(len(grid)-1, len(grid[0])-1)
        


