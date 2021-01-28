
# @Title: 丑数 (丑数 LCOF)
# @Author: 18015528893
# @Date: 2021-01-26 17:11:46
# @Runtime: 140 ms
# @Memory: 14.9 MB

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        a, b, c = 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = 2*dp[a], 3*dp[b], 5*dp[c]
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    s.nthUglyNumber(10)


