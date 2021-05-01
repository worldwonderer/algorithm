
# @Title: 整数转罗马数字 (Integer to Roman)
# @Author: 18015528893
# @Date: 2021-02-19 22:34:48
# @Runtime: 52 ms
# @Memory: 14.7 MB

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        reps = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        ans = ""
        for i, value in enumerate(values):
            while num >= value:
                ans += reps[i]
                num -= value
        return ans

