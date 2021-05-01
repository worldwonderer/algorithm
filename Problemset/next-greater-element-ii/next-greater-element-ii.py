
# @Title: 下一个更大元素 II (Next Greater Element II)
# @Author: 18015528893
# @Date: 2021-02-18 16:10:14
# @Runtime: 256 ms
# @Memory: 16.5 MB

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        nums *= 2
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                ans[idx] = nums[i]
            stack.append(i)
        return ans[:n]

