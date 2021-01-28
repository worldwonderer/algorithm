
# @Title: 数组中出现次数超过一半的数字 (数组中出现次数超过一半的数字  LCOF)
# @Author: 18015528893
# @Date: 2021-01-21 00:11:22
# @Runtime: 52 ms
# @Memory: 16.1 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 1
        m = nums[0]
        for num in nums[1:]:
            if num == m:
                c += 1
            else:
                c -= 1
                if c <= 0:
                    c = 1
                    m = num
        return m


if __name__ == '__main__':
    s= Solution()
    s.majorityElement([3, 3, 4])

