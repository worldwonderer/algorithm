
# @Title: 平衡二叉树 (平衡二叉树 LCOF)
# @Author: 18015528893
# @Date: 2021-01-27 21:59:23
# @Runtime: 64 ms
# @Memory: 19.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if root is None:
                return 0
            l = recur(root.left)
            if l == -1:
                return -1
            r = recur(root.right)
            if r == -1:
                return -1

            return max(l, r) + 1 if abs(l-r) <= 1 else -1
        return recur(root) != -1


