
# @Title: x 的平方根 (Sqrt(x))
# @Author: 18015528893
# @Date: 2021-02-23 23:03:23
# @Runtime: 44 ms
# @Memory: 14.5 MB

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 3:
            return 1
        
        l = 2
        r = x // 2 + 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if mid * mid <= x:
                l = mid
            else:
                r = mid - 1
        return l
