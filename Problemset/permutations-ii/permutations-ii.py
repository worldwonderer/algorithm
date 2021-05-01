
# @Title: 全排列 II (Permutations II)
# @Author: 18015528893
# @Date: 2021-02-22 19:18:54
# @Runtime: 52 ms
# @Memory: 15.3 MB

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(list(path))
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if nums[i] is None:
                    continue
                path.append(nums[i])
                nums[i] = None
                backtrack(path)
                nums[i] = path.pop()

        backtrack([])
        return ans


