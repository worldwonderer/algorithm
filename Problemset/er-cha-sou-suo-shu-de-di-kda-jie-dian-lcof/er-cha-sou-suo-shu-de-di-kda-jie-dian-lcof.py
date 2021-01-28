
# @Title: 二叉搜索树的第k大节点 (二叉搜索树的第k大节点  LCOF)
# @Author: 18015528893
# @Date: 2021-01-27 15:07:45
# @Runtime: 60 ms
# @Memory: 18.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    k = None
    res = None

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k

        def dfs(root):
            if root is None:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        dfs(root)
        return self.res


