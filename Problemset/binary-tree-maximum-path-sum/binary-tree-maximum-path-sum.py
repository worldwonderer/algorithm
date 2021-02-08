
# @Title: 二叉树中的最大路径和 (Binary Tree Maximum Path Sum)
# @Author: 18015528893
# @Date: 2021-02-08 14:39:39
# @Runtime: 116 ms
# @Memory: 21.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    m = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.m

    def dfs(self, root):
        if root is None:
            return 0
        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)
        self.m = max(root.val + left + right, self.m)
        return root.val + max(left, right, 0)


