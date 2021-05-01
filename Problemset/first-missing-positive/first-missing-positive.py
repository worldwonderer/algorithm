
# @Title: 缺失的第一个正数 (First Missing Positive)
# @Author: 18015528893
# @Date: 2021-02-22 12:56:47
# @Runtime: 16 ms
# @Memory: 13.1 MB

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):

            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1

