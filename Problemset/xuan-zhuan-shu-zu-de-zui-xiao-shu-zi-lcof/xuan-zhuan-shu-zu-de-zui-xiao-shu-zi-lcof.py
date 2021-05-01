
# @Title: 旋转数组的最小数字 (旋转数组的最小数字  LCOF)
# @Author: 18015528893
# @Date: 2020-09-28 22:16:10
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l = 0
        r = len(numbers) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if numbers[mid] >= numbers[0]:
                l = mid
            else:
                r = mid - 1
        if l + 1 == len(numbers):
            return numbers[0]
        else:
            return numbers[l+1]

