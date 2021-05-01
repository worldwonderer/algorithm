
# @Title: 全排列 (Permutations)
# @Author: 18015528893
# @Date: 2021-02-18 17:20:26
# @Runtime: 32 ms
# @Memory: 15.1 MB

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(list(path))
                return

            for i in range(len(nums)):
                if nums[i] is None:
                    continue
                path.append(nums[i])
                nums[i] = None
                backtrack(path)
                nums[i] = path.pop()

        backtrack([])
        return result


