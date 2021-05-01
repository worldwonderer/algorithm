
# @Title: 四数之和 (4Sum)
# @Author: 18015528893
# @Date: 2021-02-21 12:29:55
# @Runtime: 1324 ms
# @Memory: 15.3 MB

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def nSum(n, start, tar):
            res = []
            if n == 2:
                i = start
                j = len(nums)-1
                while i < j:
                    s = nums[i] + nums[j]
                    left = nums[i]
                    right = nums[j]
                    if s < tar:
                        while i < j and nums[i] == left:
                            i += 1
                    elif s > tar:
                        while i < j and nums[j] == right:
                            j -= 1
                    else:
                        print(left, right)
                        res.append([left, right])
                        while i < j and nums[i] == left:
                            i += 1
                        while i < j and nums[j] == right:
                            j -= 1
            elif n > 2:
                i = start
                while i < len(nums):
                    tuples = nSum(n-1, i+1, tar-nums[i])
                    for t in tuples:
                        t.append(nums[i])
                        res.append(t)
                    while i+1 < len(nums) and nums[i+1] == nums[i]:
                        i += 1
                    i += 1
            return res

        nums.sort()
        return nSum(4, 0, target)


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([-2,-1,-1,1,1,2,2], 4))

