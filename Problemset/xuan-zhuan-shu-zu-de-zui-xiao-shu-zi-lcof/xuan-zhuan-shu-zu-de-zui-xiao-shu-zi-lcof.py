
# @Title: 旋转数组的最小数字 (旋转数组的最小数字  LCOF)
# @Author: 18015528893
# @Date: 2020-09-28 22:16:10
# @Runtime: 48 ms
# @Memory: 13.5 MB

from typing import List


class Solution:
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

