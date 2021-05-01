
# @Title: 每日温度 (Daily Temperatures)
# @Author: 18015528893
# @Date: 2021-02-18 15:53:14
# @Runtime: 496 ms
# @Memory: 19 MB

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans


