# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            return l.val == r.val and recur(l.left, r.right) and recur(l.right, r.left)

        return root is None or (recur(root.left, root.right))
