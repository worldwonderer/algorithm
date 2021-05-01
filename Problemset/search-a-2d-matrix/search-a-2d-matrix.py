
# @Title: 搜索二维矩阵 (Search a 2D Matrix)
# @Author: 18015528893
# @Date: 2021-02-25 11:40:57
# @Runtime: 40 ms
# @Memory: 15.2 MB

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l < r:
            mid = l + (r - l) // 2
            print(mid, l, r)
            if matrix[mid][-1] >= target:
                r = mid
            else:
                l = mid + 1

        row = l
        l = 0
        r = len(matrix[row])-1

        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
        return False





