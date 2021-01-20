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
