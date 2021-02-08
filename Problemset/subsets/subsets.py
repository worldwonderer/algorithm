
# @Title: 子集 (Subsets)
# @Author: 18015528893
# @Date: 2021-02-08 21:27:33
# @Runtime: 44 ms
# @Memory: 15 MB

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrace(path, start):
            result.append(list(path))
            if len(path) == len(nums):
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrace(path, i+1)
                path.pop()

        backtrace([], 0)
        return result


