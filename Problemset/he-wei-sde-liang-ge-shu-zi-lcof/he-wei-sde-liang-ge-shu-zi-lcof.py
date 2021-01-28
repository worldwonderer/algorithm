
# @Title: 和为s的两个数字 (和为s的两个数字 LCOF)
# @Author: 18015528893
# @Date: 2021-01-28 20:31:25
# @Runtime: 116 ms
# @Memory: 25.5 MB

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [nums[i], nums[j]]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))


