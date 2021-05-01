
# @Title: 在排序数组中查找元素的第一个和最后一个位置 (Find First and Last Position of Element in Sorted Array)
# @Author: 18015528893
# @Date: 2021-02-18 14:09:07
# @Runtime: 48 ms
# @Memory: 15.5 MB

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if len(nums) == 0:
            return ans

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if nums[l] == target:
            ans[0] = l
            l = 0
            r = len(nums) - 1
            while l < r:
                mid = l + (r - l + 1) // 2
                if nums[mid] <= target:
                    l = mid
                else:
                    r = mid - 1
            if nums[l] == target:
                ans[1] = l

        return ans


