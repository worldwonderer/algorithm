
# @Title: 合并两个有序数组 (Merge Sorted Array)
# @Author: 18015528893
# @Date: 2019-10-23 01:58:40
# @Runtime: 44 ms
# @Memory: 13.5 MB

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        a = nums1[m-1]
        for num2 in nums2:
            if num2 <= a:
                while i < len(nums1):
                    if num2 > nums1[i]:
                        i += 1
                        continue
                    else:
                        nums1.insert(i, num2)
                        nums1.pop()
                        m += 1
                        break
            else:
                nums1[m] = num2
                m += 1
