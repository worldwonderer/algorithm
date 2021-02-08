
# @Title: 组合 (Combinations)
# @Author: 18015528893
# @Date: 2021-02-08 21:23:10
# @Runtime: 464 ms
# @Memory: 16.2 MB

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        choices = list(range(1, n+1))

        def backtrace(path, start):
            if len(path) == k:
                result.append(list(path))
                return
            for i in range(start, n):
                path.append(choices[i])
                backtrace(path, i+1)
                path.pop()

        backtrace([], 0)
        return result




