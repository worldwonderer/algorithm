
# @Title: 二叉树的前序遍历 (Binary Tree Preorder Traversal)
# @Author: 18015528893
# @Date: 2021-02-08 11:44:46
# @Runtime: 36 ms
# @Memory: 14.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []

        def helper(root):
            if root is None:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res


