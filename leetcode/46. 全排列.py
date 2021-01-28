from typing import List


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

if __name__ == '__main__':
    s = Solution()
    s.permute([1, 2, 3])