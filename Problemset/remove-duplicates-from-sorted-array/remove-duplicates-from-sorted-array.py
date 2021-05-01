
# @Title: 删除有序数组中的重复项 (Remove Duplicates from Sorted Array)
# @Author: 18015528893
# @Date: 2021-02-19 11:37:02
# @Runtime: 48 ms
# @Memory: 15.7 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


