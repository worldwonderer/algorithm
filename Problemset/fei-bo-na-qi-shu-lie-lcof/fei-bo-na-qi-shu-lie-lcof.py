
# @Title: 斐波那契数列 (斐波那契数列  LCOF)
# @Author: 18015528893
# @Date: 2020-09-28 21:34:44
# @Runtime: 40 ms
# @Memory: 13.3 MB

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a % 1000000007
