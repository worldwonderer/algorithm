
# @Title: 翻转单词顺序 (翻转单词顺序 LCOF)
# @Author: 18015528893
# @Date: 2021-01-29 23:04:21
# @Runtime: 64 ms
# @Memory: 15.2 MB

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i+1:j+1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)


if __name__ == '__main__':
    s = Solution()
    s.reverseWords("the sky is blue")
