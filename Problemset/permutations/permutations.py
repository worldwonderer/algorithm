
# @Title: 全排列 (Permutations)
# @Author: 18015528893
# @Date: 2021-01-28 22:14:00
# @Runtime: 56 ms
# @Memory: 14.9 MB

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, track):
            if len(track) == len(nums):
                res.append(track.copy())
                return

            for num in nums:
                if num in track:
                    continue
                track.append(num)
                backtrack(nums, track)
                track.pop()

        track = []
        backtrack(nums, track)
        return res

