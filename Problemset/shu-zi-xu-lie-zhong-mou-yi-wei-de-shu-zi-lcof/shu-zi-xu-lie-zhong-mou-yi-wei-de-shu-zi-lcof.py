
# @Title: 数字序列中某一位的数字 (数字序列中某一位的数字  LCOF)
# @Author: 18015528893
# @Date: 2021-01-24 19:47:38
# @Runtime: 32 ms
# @Memory: 14.8 MB

class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])


