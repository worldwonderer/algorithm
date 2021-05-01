
# @Title: 螺旋矩阵 (Spiral Matrix)
# @Author: 18015528893
# @Date: 2021-02-22 22:08:50
# @Runtime: 36 ms
# @Memory: 14.8 MB

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        l = 0
        u = 0
        r = len(matrix[0])-1
        d = len(matrix)-1
        ans = []
        while True:
            for i in range(l, r+1):
                ans.append(matrix[u][i])
            u += 1
            if u > d:
                break
            for i in range(u, d+1):
                ans.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l-1, -1):
                ans.append(matrix[d][i])
            d -= 1
            if u > d:
                break
            for i in range(d, u-1, -1):
                ans.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return ans
