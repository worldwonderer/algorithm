
# @Title: 两数相除 (Divide Two Integers)
# @Author: 18015528893
# @Date: 2021-02-19 22:49:05
# @Runtime: 204 ms
# @Memory: 14.8 MB

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor) > 0 or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1

        divisor = abs(divisor)
        dividend = abs(dividend)

        def mul(a, b):
            ans = 0
            while b != 0:
                if b & 1 != 0:
                    ans += a
                a <<= 1
                b >>= 1
            return ans

        l = 0
        r = dividend
        while l < r:
            mid = l + (r - l + 1) // 2
            if mul(mid, divisor) <= dividend:
                l = mid
            else:
                r = mid - 1
        ans = sign * l
        if ans > (1 << 31) - 1 or ans < -1 << 31:
            return (1 << 31) - 1
        return ans


