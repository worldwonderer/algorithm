
# @Title: 旋转图像 (Rotate Image)
# @Author: 18015528893
# @Date: 2021-02-20 11:23:34
# @Runtime: 44 ms
# @Memory: 14.8 MB

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 转置
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 每一行反转
        for i in range(n):
            matrix[i] = matrix[i][::-1]




