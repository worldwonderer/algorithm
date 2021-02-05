
# @Title: 翻转二叉树 (Invert Binary Tree)
# @Author: 18015528893
# @Date: 2021-02-05 23:13:32
# @Runtime: 40 ms
# @Memory: 14.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if root is None:
                return
            root.right, root.left = root.left, root.right
            helper(root.left)
            helper(root.right)

        helper(root)
        return root


