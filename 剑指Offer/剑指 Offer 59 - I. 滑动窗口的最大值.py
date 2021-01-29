from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []
        left = 0
        right = 0
        while right < len(nums):
            c = nums[right]
            right += 1
            window.append(c)

            while len(window) == k:
                res.append(max(window))
                left += 1
                window.popleft()
        return res


if __name__ == '__main__':
    s = Solution()
    s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
