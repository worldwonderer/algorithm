
# @Title: 回文数 (Palindrome Number)
# @Author: 18015528893
# @Date: 2019-10-21 21:41:32
# @Runtime: 84 ms
# @Memory: 13.7 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0:
            return False
        if x % 10 == 0:
            return False
        a = list()
        while True:
            a.append(x % 10)
            x = x // 10
            if x == 0:
                break
        if a[::-1] == a:
            return True
        return False
