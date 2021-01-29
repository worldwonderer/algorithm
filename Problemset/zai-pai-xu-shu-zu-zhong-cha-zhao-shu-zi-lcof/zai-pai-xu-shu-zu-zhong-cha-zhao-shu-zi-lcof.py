
# @Title: 在排序数组中查找数字 I (在排序数组中查找数字  LCOF)
# @Author: 18015528893
# @Date: 2021-01-29 14:57:47
# @Runtime: 32 ms
# @Memory: 15.6 MB

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.left_bound(nums, target+1) - self.left_bound(nums, target)

    def right_bound(self, nums, target):
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                lo = mid + 1
        return lo

    def left_bound(self, nums, target):
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                hi = mid - 1
        return hi


