
# @Title: 斐波那契数 (Fibonacci Number)
# @Author: 18015528893
# @Date: 2020-12-25 21:34:17
# @Runtime: 36 ms
# @Memory: 14.7 MB

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a

    # def fib(self, n: int) -> int:
    #     memo = [0] * (n + 1)
    #     return self.helper(memo, n)
        

    # def helper(self, memo, n):
    #     if n <= 1:
    #         return n
    #     if memo[n] != 0:
    #         return memo[n]
    #     memo[n] = self.helper(memo, n-1) + self.helper(memo, n-2)
    #     return memo[n]
