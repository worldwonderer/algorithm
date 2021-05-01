
# @Title: 搜索旋转排序数组 (Search in Rotated Sorted Array)
# @Author: 18015528893
# @Date: 2021-02-18 14:03:16
# @Runtime: 44 ms
# @Memory: 15.1 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] >= nums[0]:
                l = mid
            else:
                r = mid - 1

        if target >= nums[0]:
            r = l
            l = 0
        else:
            l += 1
            r = len(nums) -1

        while l <= r:
            mid = l + (r - l ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1


