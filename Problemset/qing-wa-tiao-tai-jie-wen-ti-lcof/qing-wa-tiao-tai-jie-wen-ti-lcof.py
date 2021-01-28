
# @Title: 青蛙跳台阶问题 (青蛙跳台阶问题  LCOF)
# @Author: 18015528893
# @Date: 2020-09-28 21:53:14
# @Runtime: 36 ms
# @Memory: 13.1 MB

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b
        return a % 1000000007
