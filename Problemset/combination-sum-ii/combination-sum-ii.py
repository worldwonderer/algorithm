
# @Title: 组合总和 II (Combination Sum II)
# @Author: 18015528893
# @Date: 2021-02-22 00:04:17
# @Runtime: 116 ms
# @Memory: 14.8 MB

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(path, start):
            s = sum(path)
            if s == target:
                ans.append(list(path))
            if s >= target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(path, i+1)
                path.pop()
        
        backtrack([], 0)
        return ans

