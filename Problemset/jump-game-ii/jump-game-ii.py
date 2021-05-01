
# @Title: 跳跃游戏 II (Jump Game II)
# @Author: 18015528893
# @Date: 2021-02-22 19:13:17
# @Runtime: 64 ms
# @Memory: 15.9 MB

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        jumps = 0
        farthest = 0
        for i in range(n-1):
            farthest = max(farthest, i+nums[i])
            if end == i:
                jumps += 1
                end = farthest
        return jumps


