
# @Title: 连续子数组的最大和 (连续子数组的最大和  LCOF)
# @Author: 18015528893
# @Date: 2021-01-21 22:50:26
# @Runtime: 64 ms
# @Memory: 18.4 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = 0
        for num in nums:
            cur_sum += num
            max_sum = max(cur_sum, max_sum)
            cur_sum = max(cur_sum, 0)
        return max_sum

