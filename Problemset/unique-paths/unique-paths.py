
# @Title: 不同路径 (Unique Paths)
# @Author: 18015528893
# @Date: 2021-02-23 22:07:05
# @Runtime: 44 ms
# @Memory: 15.3 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = dict()

        def dp(i, j):
            if i < 0:
                return 0
            if j < 0:
                return 0
            if i == 0 and j == 0:
                return 1 

            if (i, j) in memo:
                return memo[(i, j)]
            
            res = dp(i-1, j) + dp(i, j-1)
            memo[(i, j)] = res
            return res
        
        return dp(m-1, n-1)
