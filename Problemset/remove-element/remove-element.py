
# @Title: 移除元素 (Remove Element)
# @Author: 18015528893
# @Date: 2021-02-21 13:53:23
# @Runtime: 36 ms
# @Memory: 14.9 MB

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


