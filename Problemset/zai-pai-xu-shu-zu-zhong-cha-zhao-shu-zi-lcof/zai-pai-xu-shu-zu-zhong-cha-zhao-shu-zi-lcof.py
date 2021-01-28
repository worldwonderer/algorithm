
# @Title: 在排序数组中查找数字 I (在排序数组中查找数字  LCOF)
# @Author: 18015528893
# @Date: 2021-01-27 14:45:24
# @Runtime: 40 ms
# @Memory: 15.5 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target) - self.helper(nums, target-1)

    def helper(self, nums, target):
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo += 1
            else:
                hi = mid - 1
        return lo


