
# @Title: 移除元素 (Remove Element)
# @Author: 18015528893
# @Date: 2019-10-22 00:09:21
# @Runtime: 32 ms
# @Memory: 13.6 MB

class Solution:
    def removeElement(self, nums, target):
        length = len(nums)
        if length == 0:
            return 0
        i = 0
        while True:
            if nums[i] != target:
                i += 1
                if i >= length:
                    return length
            else:
                break
        if i == length-1 and nums[i] == target:
            return length-1
        j = i + 1
        while True:
            if nums[j] != target:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                j += 1
            if j >= len(nums) or i >=len(nums):
                break
        return i
