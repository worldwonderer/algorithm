
# @Title: 搜索插入位置 (Search Insert Position)
# @Author: 18015528893
# @Date: 2021-02-21 21:13:38
# @Runtime: 32 ms
# @Memory: 15.4 MB

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l

