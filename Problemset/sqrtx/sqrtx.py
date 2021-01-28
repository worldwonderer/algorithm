
# @Title: x 的平方根 (Sqrt(x))
# @Author: 18015528893
# @Date: 2019-10-23 00:09:44
# @Runtime: 40 ms
# @Memory: 13.5 MB

class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if mid * mid > x:
                hi = mid-1
            else:
                lo = mid
        return lo
