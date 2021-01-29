
# @Title: 和为s的连续正数序列 (和为s的连续正数序列 LCOF)
# @Author: 18015528893
# @Date: 2021-01-29 17:00:07
# @Runtime: 172 ms
# @Memory: 14.9 MB

from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left = 0
        right = 0
        window = 0
        l = range(1, target//2+2)
        res = list()

        while right < len(l):
            c = l[right]
            right += 1
            window += c
            while window >= target:
                if window == target:
                    res.append(list(l[left:right]))

                d = l[left]
                left += 1
                window -= d
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findContinuousSequence(15))


