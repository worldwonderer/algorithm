
# @Title: 爬楼梯 (Climbing Stairs)
# @Author: 18015528893
# @Date: 2019-10-23 01:03:57
# @Runtime: 36 ms
# @Memory: 13.6 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        l = [1, 2]
        for i in range(2, n):
            l.append(l[i-2] + l[i-1])
        return l[n-1]
