
# @Title: 分割回文串 (Palindrome Partitioning)
# @Author: 18015528893
# @Date: 2021-02-12 14:27:35
# @Runtime: 156 ms
# @Memory: 31.8 MB

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(path, begin):
            if begin == len(s):
                result.append(list(path))
                return

            for cut_length in range(1, len(s)-begin+1):
                cut_s = s[begin:begin+cut_length]
                if cut_s != cut_s[::-1]:
                    continue
                path.append(cut_s)
                begin += cut_length
                backtrack(path, begin)
                begin -= cut_length
                path.pop()

        backtrack([], 0)
        return result

