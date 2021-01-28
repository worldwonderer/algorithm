
# @Title: 树的子结构 (树的子结构  LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 20:57:30
# @Runtime: 136 ms
# @Memory: 19.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(t, s):
            if s is None:
                return True
            if t is None:
                return False
            return t.val == s.val and recur(t.left, s.left) and recur(t.right, s.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
    

