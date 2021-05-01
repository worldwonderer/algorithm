
# @Title: 下一个排列 (Next Permutation)
# @Author: 18015528893
# @Date: 2021-02-18 11:59:22
# @Runtime: 40 ms
# @Memory: 14.7 MB

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return

        i = n - 2
        j = n - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0:
            for k in range(n-1, j-1, -1):
                if nums[k] > nums[i]:
                    nums[k], nums[i] = nums[i], nums[k]
                    break

        nums[j:n] = nums[j:n][::-1]



