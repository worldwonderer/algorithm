
# @Title: 最接近的三数之和 (3Sum Closest)
# @Author: 18015528893
# @Date: 2021-02-19 11:13:39
# @Runtime: 120 ms
# @Memory: 14.9 MB

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for k in range(n):
            i = k + 1
            j = n - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if abs(s-target) < abs(ans-target):
                    ans = s
                if s == target:
                    return s
                elif s > target:
                    j -= 1
                elif s < target:
                    i += 1
        return ans


