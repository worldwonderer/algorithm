
# @Title: 二叉树中和为某一值的路径 (二叉树中和为某一值的路径 LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 21:59:00
# @Runtime: 52 ms
# @Memory: 16.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        def dfs(node, tar):
            if node is None:
                return
            path.append(node.val)
            tar -= node.val
            if node.left is None and node.right is None and tar == 0:
                res.append(list(path))
            dfs(node.left, tar)
            dfs(node.right, tar)
            path.pop()

        dfs(root, sum)
        return res


