class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        a = list(range(n))
        i = 0
        while len(a) > 1:
            i += m - 1
            i %= len(a)
            a.pop(i)
        return a[0]
