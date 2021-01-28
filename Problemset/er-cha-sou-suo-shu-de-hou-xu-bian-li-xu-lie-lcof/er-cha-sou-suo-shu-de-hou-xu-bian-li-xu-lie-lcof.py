
# @Title: 二叉搜索树的后序遍历序列 (二叉搜索树的后序遍历序列 LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 21:49:53
# @Runtime: 40 ms
# @Memory: 14.8 MB

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j:
                return True
            m = i
            while postorder[m] < postorder[j]:
                m += 1
            n = m
            while postorder[m] > postorder[j]:
                m += 1
            return m == j and recur(i, n-1) and recur(n, j-1)
        return recur(0, len(postorder)-1)


