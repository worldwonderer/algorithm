
# @Title: 扑克牌中的顺子 (扑克牌中的顺子  LCOF)
# @Author: 18015528893
# @Date: 2021-02-01 19:16:12
# @Runtime: 44 ms
# @Memory: 14.7 MB

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        s = set()
        max_ = -1
        min_ = 14
        for n in nums:
            if n == 0:
                continue
            if n in s:
                return False
            else:
                s.add(n)
            max_ = max(max_, n)
            min_ = min(min_, n)
        return max_ - min_ < 5

