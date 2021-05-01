
# @Title: 三数之和 (3Sum)
# @Author: 18015528893
# @Date: 2021-02-18 10:51:43
# @Runtime: 1152 ms
# @Memory: 18 MB

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def twoSum(lo, hi, target):
            res = []
            while lo < hi:
                s = nums[lo] + nums[hi]
                left = nums[lo]
                right = nums[hi]
                if s == target:
                    res.append([nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                elif s > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                else:
                    while lo < hi and nums[lo] == left:
                        lo += 1
            return res

        i = 0
        while i < len(nums):
            tuples = twoSum(i+1, len(nums)-1, -nums[i])

            for t in tuples:
                t.append(nums[i])
                ans.append(t)

            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return ans


