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
