
# @Title: 二叉树展开为链表 (Flatten Binary Tree to Linked List)
# @Author: 18015528893
# @Date: 2021-02-05 23:27:59
# @Runtime: 36 ms
# @Memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left
        
        p = root
        while p.right:
            p = p.right
        p.right = right


