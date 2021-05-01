
# @Title: 最后一个单词的长度 (Length of Last Word)
# @Author: 18015528893
# @Date: 2021-02-23 11:10:55
# @Runtime: 36 ms
# @Memory: 14.9 MB

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = len(s) - 1
        ans = 0
        while i >= 0 and s[i] != " ":
            ans += 1
            i -= 1
        
        return ans

