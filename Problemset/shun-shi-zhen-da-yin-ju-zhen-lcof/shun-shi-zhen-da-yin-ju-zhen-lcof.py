
# @Title: 顺时针打印矩阵 (顺时针打印矩阵  LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 21:18:24
# @Runtime: 40 ms
# @Memory: 15.3 MB

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        res = []
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        while True:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res

