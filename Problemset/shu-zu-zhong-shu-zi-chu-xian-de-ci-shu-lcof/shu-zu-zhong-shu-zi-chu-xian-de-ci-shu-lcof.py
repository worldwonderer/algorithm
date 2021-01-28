
# @Title: 数组中数字出现的次数 (数组中数字出现的次数 LCOF)
# @Author: 18015528893
# @Date: 2021-01-27 22:13:09
# @Runtime: 60 ms
# @Memory: 15.6 MB

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        x, y, n, m = 0, 0, 0, 1
        for num in nums:
            n ^= num
        while n & m == 0:
            m <<= 1
        for num in nums:
            if num & m:
                x ^= num
            else:
                y ^= num
        return x, y


