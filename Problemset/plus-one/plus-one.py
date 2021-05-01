
# @Title: 加一 (Plus One)
# @Author: 18015528893
# @Date: 2021-02-23 22:33:00
# @Runtime: 40 ms
# @Memory: 14.8 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

        if digits[0] == 0:
            return digits[1:]
        else:
            return digits
