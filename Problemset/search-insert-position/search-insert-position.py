
# @Title: 搜索插入位置 (Search Insert Position)
# @Author: 18015528893
# @Date: 2019-10-22 12:39:30
# @Runtime: 68 ms
# @Memory: 13.9 MB

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if len(nums) == 0:
            return 0
        if target > nums[-1]:
            return size
        lo = 0
        hi = size
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
