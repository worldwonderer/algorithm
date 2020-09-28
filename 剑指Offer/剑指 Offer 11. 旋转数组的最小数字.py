from typing import List


class Solution:
    """
    二分法，用nums[m]与nums[j]比较
    """
    def minArray(self, numbers: List[int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] < numbers[j]:
                j = m
            elif numbers[m] > numbers[j]:
                i = m + 1
            else:
                j -= 1
        return numbers[i]
