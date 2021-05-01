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
