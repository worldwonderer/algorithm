
# @Title: 圆圈中最后剩下的数字 (圆圈中最后剩下的数字 LCOF)
# @Author: 18015528893
# @Date: 2021-02-01 19:59:46
# @Runtime: 2168 ms
# @Memory: 18.1 MB

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        a = list(range(n))
        i = 0
        while len(a) > 1:
            i += m - 1
            i %= len(a)
            a.pop(i)
        return a[0]
