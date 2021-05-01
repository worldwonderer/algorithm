
# @Title: 二叉树的直径 (Diameter of Binary Tree)
# @Author: 18015528893
# @Date: 2021-02-14 21:46:53
# @Runtime: 52 ms
# @Memory: 16.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        m = 0
        def dfs(root):
            nonlocal m
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            m = max(m, l+r)
            return max(l, r) + 1
        
        dfs(root)
        return m
