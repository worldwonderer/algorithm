
# @Title: 最大子序和 (Maximum Subarray)
# @Author: 18015528893
# @Date: 2021-02-18 20:24:39
# @Runtime: 52 ms
# @Memory: 15.3 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        s = 0
        for num in nums:
            if s < 0:
                s = num
            else:
                s += num
            max_sum = max(max_sum, s)
        return max_sum

