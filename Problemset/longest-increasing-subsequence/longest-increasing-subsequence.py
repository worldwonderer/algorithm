
# @Title: 最长递增子序列 (Longest Increasing Subsequence)
# @Author: 18015528893
# @Date: 2020-12-25 22:32:17
# @Runtime: 3744 ms
# @Memory: 14.8 MB

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(dp)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

