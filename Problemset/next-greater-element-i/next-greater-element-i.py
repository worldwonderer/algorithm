
# @Title: 下一个更大元素 I (Next Greater Element I)
# @Author: 18015528893
# @Date: 2021-02-18 15:39:53
# @Runtime: 44 ms
# @Memory: 15.1 MB

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        m = {}
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                m[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        while stack:
            m[stack.pop()] = -1

        return [m[x] for x in nums1]

