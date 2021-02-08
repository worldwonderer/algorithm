
# @Title: 组合总和 (Combination Sum)
# @Author: 18015528893
# @Date: 2021-02-08 18:22:44
# @Runtime: 116 ms
# @Memory: 15 MB

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrace(path, start):
            s = sum(path)
            if s == target:
                result.append(list(path))
                return
            if s > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrace(path, i)
                path.pop()
        backtrace([], 0)
        return result

