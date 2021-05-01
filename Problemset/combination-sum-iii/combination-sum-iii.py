
# @Title: 组合总和 III (Combination Sum III)
# @Author: 18015528893
# @Date: 2021-02-12 14:20:59
# @Runtime: 32 ms
# @Memory: 14.8 MB

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        result = []

        def backtrack(path, start):
            s = sum(path)
            if len(path) == k and s == n:
                result.append(list(path))
            if len(path) >= k:
                return
            if s >= n:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(path, i+1)
                path.pop()
        
        backtrack([], 0)
        return result

