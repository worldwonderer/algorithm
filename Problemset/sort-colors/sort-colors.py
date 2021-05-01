
# @Title: 颜色分类 (Sort Colors)
# @Author: 18015528893
# @Date: 2021-02-28 11:26:01
# @Runtime: 52 ms
# @Memory: 15 MB

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        # [0, p0) = 0
        # [p0, i) = 1
        # (p2, len-1] = 2
        
        p0 = 0
        p2 = len(nums)-1
        i = 0

        while i <= p2:
            if nums[i] == 0:
                nums[i] = 0
                p0 += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1

            
        

            
