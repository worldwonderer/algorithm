
# @Title: 合并二叉树 (Merge Two Binary Trees)
# @Author: 18015528893
# @Date: 2021-02-14 16:12:11
# @Runtime: 76 ms
# @Memory: 15.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        def dfs(p, q):
            if p is None and q is None:
                return
            elif p is None:
                return q
            elif q is None:
                return p
            else:
                root = TreeNode(p.val + q.val)
                root.left = dfs(p.left, q.left)
                root.right = dfs(p.right, q.right)
                return root
        
        return dfs(root1, root2)
