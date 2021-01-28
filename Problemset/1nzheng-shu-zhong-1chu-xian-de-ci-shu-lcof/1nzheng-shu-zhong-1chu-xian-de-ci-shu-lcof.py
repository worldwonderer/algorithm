
# @Title: 1～n 整数中 1 出现的次数 (1～n整数中1出现的次数  LCOF)
# @Author: 18015528893
# @Date: 2021-01-24 19:09:42
# @Runtime: 28 ms
# @Memory: 14.8 MB

class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        digit = 1
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += high * digit + digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res


