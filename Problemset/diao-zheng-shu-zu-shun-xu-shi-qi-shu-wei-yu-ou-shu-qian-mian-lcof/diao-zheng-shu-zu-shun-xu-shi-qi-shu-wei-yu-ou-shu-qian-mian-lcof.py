
# @Title: 调整数组顺序使奇数位于偶数前面 (调整数组顺序使奇数位于偶数前面 LCOF)
# @Author: 18015528893
# @Date: 2021-01-17 22:22:28
# @Runtime: 60 ms
# @Memory: 18.8 MB

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] % 2 == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums

