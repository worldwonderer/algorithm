
# @Title: 二叉树中的最大路径和 (Binary Tree Maximum Path Sum)
# @Author: 18015528893
# @Date: 2021-02-14 11:38:20
# @Runtime: 112 ms
# @Memory: 22.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        m = float('-inf')
        def dfs(root):
            nonlocal m 
            if root is None:
                return 0
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)
            m = max(m, root.val + left_max + right_max)
            return root.val + max(left_max, right_max, 0)

        dfs(root)
        return m




        
