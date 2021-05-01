
# @Title: 二叉树的最近公共祖先 (Lowest Common Ancestor of a Binary Tree)
# @Author: 18015528893
# @Date: 2021-02-14 17:34:07
# @Runtime: 68 ms
# @Memory: 25.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or p == root or q == root:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None and right is None:
            return
        if left is None:
            return right
        if right is None:
            return left
        return root

