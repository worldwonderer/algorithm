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
