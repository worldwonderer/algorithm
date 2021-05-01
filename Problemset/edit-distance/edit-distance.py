
# @Title: 编辑距离 (Edit Distance)
# @Author: 18015528893
# @Date: 2021-02-24 10:31:33
# @Runtime: 112 ms
# @Memory: 17.5 MB

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if word1[i] ==  word2[j]:
                res = dp(i-1, j-1)
            else:
                res = min(
                    dp(i, j-1)+1,  # 插入
                    dp(i-1, j)+1,  # 删除
                    dp(i-1, j-1) + 1  # 替换
                )
            memo[(i, j)] = res
            return res

        return dp(len(word1)-1, len(word2)-1)



