
# @Title: 构建乘积数组 (构建乘积数组 LCOF)
# @Author: 18015528893
# @Date: 2021-02-02 21:28:08
# @Runtime: 68 ms
# @Memory: 22.5 MB

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        b = [1] * n
        right = 1
        for i in range(1, n):
            b[i] = b[i-1] * a[i-1]
        for i in range(n-2, -1, -1):
            right *= a[i+1]
            b[i] *= right
        return b

