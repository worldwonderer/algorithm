
# @Title: 删除排序数组中的重复项 (Remove Duplicates from Sorted Array)
# @Author: 18015528893
# @Date: 2019-10-21 23:40:55
# @Runtime: 96 ms
# @Memory: 15 MB

class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 0
        j = 0
        while True:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
            if j >= len(nums):
                break
        return i+1
            
