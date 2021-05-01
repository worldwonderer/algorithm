
# @Title: 数组中重复的数字 (数组中重复的数字 LCOF)
# @Author: 18015528893
# @Date: 2021-02-28 16:44:53
# @Runtime: 52 ms
# @Memory: 23.4 MB

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
