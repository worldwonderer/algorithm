
# @Title: 对称二叉树 (Symmetric Tree)
# @Author: 18015528893
# @Date: 2021-02-14 21:30:57
# @Runtime: 44 ms
# @Memory: 15.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
            
        def dfs(p, q):
            if p is None and q is None:
                return True
            if p is None:
                return False
            if q is None:
                return False
            return p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left)

        return dfs(root.left, root.right)
        
        

