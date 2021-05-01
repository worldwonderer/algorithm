
# @Title: 二分查找 (Binary Search)
# @Author: 18015528893
# @Date: 2021-02-16 19:47:16
# @Runtime: 248 ms
# @Memory: 16 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
        return lo if len(nums)-1 >= lo >= 0 and nums[lo] == target else -1

