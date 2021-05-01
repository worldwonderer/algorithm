
# @Title: 串联所有单词的子串 (Substring with Concatenation of All Words)
# @Author: 18015528893
# @Date: 2021-02-21 21:07:53
# @Runtime: 804 ms
# @Memory: 15.1 MB

from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        need = defaultdict(int)
        for word in words:
            need[word] += 1
        word_length = len(words[0])
        word_count = len(words)
        total = word_length * word_count
        for i in range(len(s)-total+1):
            window = defaultdict(int)
            for j in range(i, i+total, word_length):
                window[s[j:j+word_length]] += 1
            if window == need:
                ans.append(i)
        return ans

