
# @Title: 滑动窗口的最大值 (滑动窗口的最大值 LCOF)
# @Author: 18015528893
# @Date: 2021-02-13 23:03:25
# @Runtime: 452 ms
# @Memory: 18.2 MB

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = right = 0
        window = deque()
        while right < len(nums):
            c = nums[right]
            right += 1
            window.append(c)

            while len(window) > k:
                left -= 1
                window.popleft()

            if len(window) == k:
                result.append(max(window))
        return result
