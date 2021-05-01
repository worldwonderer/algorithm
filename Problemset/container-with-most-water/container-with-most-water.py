
# @Title: 盛最多水的容器 (Container With Most Water)
# @Author: 18015528893
# @Date: 2021-02-18 00:23:56
# @Runtime: 68 ms
# @Memory: 16.2 MB

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j-i))
                i += 1
            else:
                res = max(res, height[j] * (j-i))
                j -= 1
        return res

