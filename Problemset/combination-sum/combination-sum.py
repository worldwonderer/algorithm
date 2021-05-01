
# @Title: 组合总和 (Combination Sum)
# @Author: 18015528893
# @Date: 2021-02-18 14:13:06
# @Runtime: 80 ms
# @Memory: 14.8 MB

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(path, start):
            s = sum(path)
            if s == target:
                ans.append(list(path))
            if s >= target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(path, i)
                path.pop()

        backtrack([], 0)
        return ans


