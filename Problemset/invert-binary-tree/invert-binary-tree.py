
# @Title: 翻转二叉树 (Invert Binary Tree)
# @Author: 18015528893
# @Date: 2021-02-14 11:53:27
# @Runtime: 44 ms
# @Memory: 14.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return root

