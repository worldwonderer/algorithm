
# @Title: 寻找两个正序数组的中位数 (Median of Two Sorted Arrays)
# @Author: 18015528893
# @Date: 2021-02-17 18:38:03
# @Runtime: 48 ms
# @Memory: 15 MB

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        total_left = (m + n + 1) // 2
        l = 0
        r = m
        while l < r:
            i = l + (r - l + 1) // 2
            j = total_left - i
            if nums1[i-1] <= nums2[j]:
                l = i
            else:
                r = i - 1
        
        i = l
        j = total_left - i
        left_nums1_max = float('-inf') if i == 0 else nums1[i-1]
        left_nums2_max = float('-inf') if j == 0 else nums2[j-1]
        right_nums1_min = float('inf') if i == m else nums1[i]
        right_nums2_min = float('inf') if j == n else nums2[j]

        if (m + n) % 2 == 1:
            return max(left_nums1_max, left_nums2_max)
        else:
            return (max(left_nums1_max, left_nums2_max) + min(right_nums1_min, right_nums2_min)) / 2

