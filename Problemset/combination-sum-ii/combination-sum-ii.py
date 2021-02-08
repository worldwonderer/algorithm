
# @Title: 组合总和 II (Combination Sum II)
# @Author: 18015528893
# @Date: 2021-02-08 21:10:16
# @Runtime: 92 ms
# @Memory: 15 MB

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrace(path, start):
            s = sum(path)
            if s == target:
                result.append(list(path))
                return
            if s > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                backtrace(path, i+1)
                path.pop()
        backtrace([], 0)
        return result


