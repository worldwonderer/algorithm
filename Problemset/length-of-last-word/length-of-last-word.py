
# @Title: 最后一个单词的长度 (Length of Last Word)
# @Author: 18015528893
# @Date: 2019-10-22 22:50:38
# @Runtime: 36 ms
# @Memory: 13.6 MB

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = None
        e = None
        for i in range(len(s)-1, -1, -1):
            if e is None and s[i] != ' ':
                e = i
            if e is not None and st is None and s[i] == ' ':
                st = i 
            if st and e:
                break
        if e is None:
            return 0
        if st is None:
            st = -1
        return e - st
