
# @Title: 子集 (Subsets)
# @Author: 18015528893
# @Date: 2021-02-28 12:23:12
# @Runtime: 44 ms
# @Memory: 15.2 MB

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, start):
            result.append(list(path))

            if len(path) >= len(nums):
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
        
        backtrack([], 0)
        return result

