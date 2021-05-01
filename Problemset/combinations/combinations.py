
# @Title: 组合 (Combinations)
# @Author: 18015528893
# @Date: 2021-02-28 12:21:11
# @Runtime: 416 ms
# @Memory: 16.2 MB

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = list(range(1, n+1))

        def backtrack(path, start):
            if len(path) == k:
                result.append(list(path))
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
        
        backtrack([], 0)
        return result

