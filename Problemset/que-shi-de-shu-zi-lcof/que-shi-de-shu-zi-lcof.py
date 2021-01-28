
# @Title: 0～n-1中缺失的数字 (缺失的数字  LCOF)
# @Author: 18015528893
# @Date: 2021-01-27 14:48:47
# @Runtime: 48 ms
# @Memory: 15.8 MB

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == mid:
                lo += 1
            else:
                hi = mid - 1
        return lo


