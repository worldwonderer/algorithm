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
