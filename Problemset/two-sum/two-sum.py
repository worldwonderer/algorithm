
# @Title: 两数之和 (Two Sum)
# @Author: 18015528893
# @Date: 2021-04-12 14:33:59
# @Runtime: 32 ms
# @Memory: 14.9 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = dict()
        for i in range(len(nums)):
            if target - nums[i] in memo:
                return [i, memo[target-nums[i]]]
            memo[nums[i]] = i
         
