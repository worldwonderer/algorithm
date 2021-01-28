
# @Title: 两数之和 (Two Sum)
# @Author: 18015528893
# @Date: 2019-10-21 21:09:09
# @Runtime: 72 ms
# @Memory: 14.8 MB

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        m = dict()
        for ind, num in enumerate(nums):
            m[num] = ind
            
        for ind, num in enumerate(nums):
            if target-num in m and m[target-num] != ind:
                return [ind, m[target-num]]
        """
        
        m = dict()
        for ind, num in enumerate(nums):
            if target-num in m:
                return [ind, m[target-num]]
            m[num] = ind
                
