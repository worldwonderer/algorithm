
# @Title: 数组中数字出现的次数 II (数组中数字出现的次数 II LCOF)
# @Author: 18015528893
# @Date: 2021-01-28 20:22:52
# @Runtime: 240 ms
# @Memory: 15.7 MB

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            count = 0
            index = 1 << i
            for num in nums:
                if num & index != 0:
                    count += 1
            if count % 3 == 1:
                result |= index
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([3, 4, 3, 3]))


