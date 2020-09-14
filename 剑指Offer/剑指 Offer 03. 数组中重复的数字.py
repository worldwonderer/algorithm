from typing import List


class Solution:
    """
    因为出现的元素值 < len(nums)
    所以我们可以将见到的元素放到索引的位置，如果交换时，发现索引处已存在该元素，则重复
    O(N) 空间O(1)
    """
    def findRepeatNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            while True:
                m = nums[i]
                if m == i:
                    break
                if m != i and nums[m] == m:
                    return m
                else:
                    nums[m], nums[i] = nums[i], nums[m]
        return -1
