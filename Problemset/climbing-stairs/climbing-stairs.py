
# @Title: 爬楼梯 (Climbing Stairs)
# @Author: 18015528893
# @Date: 2021-02-18 20:22:35
# @Runtime: 44 ms
# @Memory: 14.8 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(n-2):
            a, b = b, a + b
        return b

