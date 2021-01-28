
# @Title: 加一 (Plus One)
# @Author: 18015528893
# @Date: 2019-10-22 23:04:26
# @Runtime: 32 ms
# @Memory: 13.4 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            i = -2
            while True:
                try:
                    if digits[i] == 9:
                        digits[i] = 0
                        i -= 1
                    else:
                        digits[i] += 1
                        break
                except IndexError:
                    digits.insert(0, 1)
                    break
        return digits
                
