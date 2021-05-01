
# @Title: 寻找旋转排序数组中的最小值 (Find Minimum in Rotated Sorted Array)
# @Author: 18015528893
# @Date: 2021-02-17 14:00:23
# @Runtime: 32 ms
# @Memory: 15 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] >= nums[0]:
                l = mid
            else:
                r = mid - 1
        return nums[0] if l+1 == len(nums) else nums[l+1] 

