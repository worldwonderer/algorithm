
# @Title: 二叉树的深度 (二叉树的深度 LCOF)
# @Author: 18015528893
# @Date: 2021-02-14 21:36:48
# @Runtime: 56 ms
# @Memory: 16.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

