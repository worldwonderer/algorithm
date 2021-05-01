
# @Title: 平衡二叉树 (平衡二叉树 LCOF)
# @Author: 18015528893
# @Date: 2021-02-15 23:46:26
# @Runtime: 52 ms
# @Memory: 19.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if root is None:
                return 0
            left = helper(root.left)
            if left == -1:
                return -1
            right = helper(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left-right) <= 1 else -1
        return helper(root) != -1
