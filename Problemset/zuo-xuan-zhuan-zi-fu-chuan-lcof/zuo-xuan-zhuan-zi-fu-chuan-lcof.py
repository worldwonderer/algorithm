
# @Title: 左旋转字符串 (左旋转字符串 LCOF)
# @Author: 18015528893
# @Date: 2021-01-29 23:07:43
# @Runtime: 36 ms
# @Memory: 14.9 MB

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

