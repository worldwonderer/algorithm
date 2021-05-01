
# @Title: 树的子结构 (树的子结构  LCOF)
# @Author: 18015528893
# @Date: 2021-02-14 22:12:00
# @Runtime: 128 ms
# @Memory: 19.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False
        if A is None:
            return False
        def dfs(p, q):
            if q is None:
                return True
            if p is None:
                return False
            return p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right)
        return dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

