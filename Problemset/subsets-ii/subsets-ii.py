
# @Title: 子集 II (Subsets II)
# @Author: 18015528893
# @Date: 2021-02-11 23:37:47
# @Runtime: 32 ms
# @Memory: 15.2 MB

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrace(path, start):
            result.append(list(path))
            if len(path) == len(nums):
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrace(path, i+1)
                path.pop()

        backtrace([], 0)
        return result


