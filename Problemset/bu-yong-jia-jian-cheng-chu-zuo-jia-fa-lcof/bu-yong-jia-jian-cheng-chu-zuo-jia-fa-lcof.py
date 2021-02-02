
# @Title: 不用加减乘除做加法 (不用加减乘除做加法 LCOF)
# @Author: 18015528893
# @Date: 2021-02-02 21:42:12
# @Runtime: 32 ms
# @Memory: 14.8 MB

class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a &= x
        b &= x
        while b != 0:
            carry = (a & b) << 1 & x  # 无进位的和为异或值，进位为与操作左移1位；
            total = a ^ b
            a = total
            b = carry
        return a if a <= 0x7fffffff else ~(a ^ x)

