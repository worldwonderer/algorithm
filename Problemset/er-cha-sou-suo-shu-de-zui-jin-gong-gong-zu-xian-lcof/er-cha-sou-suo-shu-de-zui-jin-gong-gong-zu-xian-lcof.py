
# @Title: 二叉搜索树的最近公共祖先 (二叉搜索树的最近公共祖先 LCOF)
# @Author: 18015528893
# @Date: 2021-02-02 20:42:50
# @Runtime: 88 ms
# @Memory: 18.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if q.val > root.val and p.val > root.val:
                root = root.right
            elif q.val < root.val and p.val < root.val:
                root = root.left
            else:
                break
        return root

