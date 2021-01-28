
# @Title: 把数组排成最小的数 (把数组排成最小的数 LCOF)
# @Author: 18015528893
# @Date: 2021-01-24 20:06:14
# @Runtime: 48 ms
# @Memory: 14.8 MB

import functools


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        nums_2_strs = [str(num) for num in nums]
        nums_2_strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(nums_2_strs)

