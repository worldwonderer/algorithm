
# @Title: Pow(x, n) (Pow(x, n))
# @Author: 18015528893
# @Date: 2021-02-22 20:30:25
# @Runtime: 36 ms
# @Memory: 14.8 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.:
            return 0.
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        while n != 0:
            if n & 1 != 0:
                ans *= x
            x = x * x
            n >>= 1
        return ans

