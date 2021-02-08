
# @Title: 平衡二叉树 (Balanced Binary Tree)
# @Author: 18015528893
# @Date: 2021-02-08 11:33:55
# @Runtime: 68 ms
# @Memory: 19.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def get_height(root):
            if root is None:
                return 0
            return max(get_height(root.left), get_height(root.right)) + 1

        return abs(get_height(root.left) - get_height(root.right)) <= 1 \
               and self.isBalanced(root.left) and self.isBalanced(root.right)


