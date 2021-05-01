
# @Title: 矩阵置零 (Set Matrix Zeroes)
# @Author: 18015528893
# @Date: 2021-02-24 14:33:15
# @Runtime: 52 ms
# @Memory: 15.1 MB

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row0_flag = False
        col0_flag = False

        for i in range(n):
            if matrix[0][i] == 0:
                row0_flag = True

        for i in range(m):
            if matrix[i][0] == 0:
                col0_flag = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for i in range(n):
                matrix[0][i] = 0

        if col0_flag:
            for i in range(m):
                matrix[i][0] = 0

