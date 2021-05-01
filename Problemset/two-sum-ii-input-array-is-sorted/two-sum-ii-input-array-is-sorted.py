
# @Title: 两数之和 II - 输入有序数组 (Two Sum II - Input array is sorted)
# @Author: 18015528893
# @Date: 2021-02-15 23:53:02
# @Runtime: 40 ms
# @Memory: 15.3 MB

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            s = numbers[lo] + numbers[hi]
            left = numbers[lo]
            right = numbers[hi]
            if s < target:
                while lo < hi and numbers[lo] == left:
                    lo += 1
            elif s > target:
                while lo < hi and numbers[hi] == right:
                    hi -= 1
            else:
                return [lo+1, hi+1]

