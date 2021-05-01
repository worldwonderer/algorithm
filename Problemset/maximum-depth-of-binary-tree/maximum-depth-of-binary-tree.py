
# @Title: 二叉树的最大深度 (Maximum Depth of Binary Tree)
# @Author: 18015528893
# @Date: 2021-02-14 16:13:48
# @Runtime: 48 ms
# @Memory: 16.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

