
# @Title: 机器人的运动范围 (机器人的运动范围  LCOF)
# @Author: 18015528893
# @Date: 2021-01-07 20:33:15
# @Runtime: 76 ms
# @Memory: 15.5 MB

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()

        def dfs(i, j):
            s = sum(int(x) for x in str(i) + str(j))
            if not 0 <= i < m or not 0 <= j < n or s > k or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)

