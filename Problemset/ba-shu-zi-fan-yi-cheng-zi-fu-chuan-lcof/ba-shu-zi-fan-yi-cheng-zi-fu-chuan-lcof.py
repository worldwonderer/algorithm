
# @Title: 把数字翻译成字符串 (把数字翻译成字符串 LCOF)
# @Author: 18015528893
# @Date: 2021-01-25 20:20:27
# @Runtime: 36 ms
# @Memory: 14.9 MB

class Solution:
    def translateNum(self, num: int) -> int:
        memo = dict()

        def dp(i):
            if i in memo:
                return memo[i]
            if i <= 0:
                return 1
            if 10 <= int(str(num)[i-1] + str(num)[i]) <= 25:
                memo[i] = dp(i-1) + dp(i-2)
            else:
                memo[i] = dp(i-1)
            return memo[i]

        return dp(len(str(num))-1)


