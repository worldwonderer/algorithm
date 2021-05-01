
# @Title: 跳跃游戏 (Jump Game)
# @Author: 18015528893
# @Date: 2021-02-22 00:17:58
# @Runtime: 48 ms
# @Memory: 16 MB

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        last = len(nums) - 1
        for i in range(len(nums)):
            jump = nums[i]
            if max_i >= i:
                max_i = max(max_i, i+jump)
                if max_i >= last:
                    return True
        return False
