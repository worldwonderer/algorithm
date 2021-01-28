
# @Title: 二叉树的镜像 (二叉树的镜像  LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 21:00:02
# @Runtime: 56 ms
# @Memory: 14.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

