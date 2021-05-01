
# @Title: 搜索旋转排序数组 II (Search in Rotated Sorted Array II)
# @Author: 18015528893
# @Date: 2021-02-28 15:49:26
# @Runtime: 40 ms
# @Memory: 15.4 MB

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        right = len(nums) - 1
        while right >= 1 and nums[right] == nums[0]:
            right -= 1

        r = right
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
            r = right

        while l <= r:
            mid = l + (r - l ) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

