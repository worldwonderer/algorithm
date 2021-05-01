
# @Title: 螺旋矩阵 II (Spiral Matrix II)
# @Author: 18015528893
# @Date: 2021-02-23 11:28:01
# @Runtime: 52 ms
# @Memory: 14.9 MB

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        l = 0
        u = 0
        d = n-1
        r = n-1
        num_to_fill = 1
        while True:
            for i in range(l, r+1):
                ans[u][i] = num_to_fill
                num_to_fill += 1
            u += 1
            if u > d:
                break
            for i in range(u, d+1):
                ans[i][r] = num_to_fill
                num_to_fill += 1
            r -= 1
            if l > r:
                break
            for i in range(r, l-1, -1):
                ans[d][i] = num_to_fill
                num_to_fill += 1
            d -= 1
            if u > d:
                break
            for i in range(d, u-1, -1):
                ans[i][l] = num_to_fill
                num_to_fill += 1
            l += 1
            if l > r:
                break
        return ans


