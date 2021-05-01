
# @Title: 最长公共前缀 (Longest Common Prefix)
# @Author: 18015528893
# @Date: 2021-02-19 11:01:48
# @Runtime: 48 ms
# @Memory: 15 MB

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                ans += tmp[0]
            else:
                break
        return ans



