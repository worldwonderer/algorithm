
# @Title: 接雨水 (Trapping Rain Water)
# @Author: 18015528893
# @Date: 2021-02-18 17:16:40
# @Runtime: 32 ms
# @Memory: 15 MB

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        ans = 0
        stack = []
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                idx = stack.pop()

                while stack and height[stack[-1]] == height[idx]:
                    stack.pop()

                if stack:
                    left = height[stack[-1]]
                    cur = height[idx]
                    right = height[i]
                    ans += (min(left, right) - cur) * (i-stack[-1]-1)
            stack.append(i)
        return ans


