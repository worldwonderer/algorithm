from typing import List


class Solution:
    """
    站在右上角看
    这个矩阵其实就像是一个Binary Search Tree
    """
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix) and len(matrix[0])
        while row < len(matrix) and col > 0:
            if matrix[row][col-1] == target:
                return True
            elif matrix[row][col-1] > target:
                col -= 1
            else:
                row += 1
        return False
