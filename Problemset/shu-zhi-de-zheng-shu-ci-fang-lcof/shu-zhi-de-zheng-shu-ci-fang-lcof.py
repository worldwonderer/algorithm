
# @Title: 数值的整数次方 (数值的整数次方 LCOF)
# @Author: 18015528893
# @Date: 2021-01-17 18:55:49
# @Runtime: 36 ms
# @Memory: 14.9 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / x * self.myPow(1 / x, -n - 1)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)

