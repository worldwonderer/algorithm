
# @Title: 最大子序和 (Maximum Subarray)
# @Author: 18015528893
# @Date: 2019-10-22 13:23:18
# @Runtime: 96 ms
# @Memory: 14.4 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        i = 0
        tmp = 0
        while True:
            tmp += nums[i]
            if tmp < 0:
                if tmp > m:
                    m = tmp
                tmp = 0
            else:
                if tmp > m:
                    m = tmp
            i += 1
            if i >= len(nums):
                break
        return m
