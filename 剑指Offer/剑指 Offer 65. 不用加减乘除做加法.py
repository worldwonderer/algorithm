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
