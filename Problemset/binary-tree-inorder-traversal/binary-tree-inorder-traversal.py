
# @Title: 二叉树的中序遍历 (Binary Tree Inorder Traversal)
# @Author: 18015528893
# @Date: 2021-02-05 22:49:47
# @Runtime: 32 ms
# @Memory: 14.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if root is None:
            return []

        def helper(root):
            if root is None:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res



