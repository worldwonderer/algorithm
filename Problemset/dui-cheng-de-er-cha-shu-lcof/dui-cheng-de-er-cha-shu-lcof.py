
# @Title: 对称的二叉树 (对称的二叉树  LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 21:04:25
# @Runtime: 40 ms
# @Memory: 15.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            return l.val == r.val and recur(l.left, r.right) and recur(l.right, r.left)

        return root is None or (recur(root.left, root.right))

