
# @Title: 二叉树的最近公共祖先 (二叉树的最近公共祖先 LCOF)
# @Author: 18015528893
# @Date: 2021-02-02 20:48:22
# @Runtime: 88 ms
# @Memory: 25.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if right is None and left is None:
            return None
        elif right is None:
            return left
        elif left is None:
            return right
        return root
