
# @Title: 删除有序数组中的重复项 II (Remove Duplicates from Sorted Array II)
# @Author: 18015528893
# @Date: 2021-02-28 15:10:58
# @Runtime: 44 ms
# @Memory: 15 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for i in range(len(nums)):
            if l < 2 or nums[i] != nums[l-2]:
                nums[l] = nums[i]
                l += 1
        return l

