
# @Title: 二进制中1的个数 (二进制中1的个数 LCOF)
# @Author: 18015528893
# @Date: 2021-01-17 18:35:28
# @Runtime: 56 ms
# @Memory: 14.9 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1  # 消去最右边的1
        return res

