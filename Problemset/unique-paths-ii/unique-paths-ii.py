
# @Title: 不同路径 II (Unique Paths II)
# @Author: 18015528893
# @Date: 2021-02-23 22:15:54
# @Runtime: 48 ms
# @Memory: 15 MB

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = dict()

        def dp(i, j):
            if i < 0:
                return 0
            if j < 0:
                return 0
            if i == 0 and j == 0:
                if obstacleGrid[0][0] == 1:
                    return 0
                else:
                    return 1

            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            if obstacleGrid[i-1][j] == 0:
                res += dp(i-1, j)
            if obstacleGrid[i][j-1] == 0:
                res += dp(i, j-1)
            memo[(i, j)] = res
            return res
        
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:
            return 0
        else:
            return dp(len(obstacleGrid)-1, len(obstacleGrid[0])-1)

