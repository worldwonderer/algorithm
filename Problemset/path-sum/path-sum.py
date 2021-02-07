
# @Title: 路径总和 (Path Sum)
# @Author: 18015528893
# @Date: 2021-02-07 22:21:28
# @Runtime: 44 ms
# @Memory: 16.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        res = []

        def dfs(root, path, k):
            if root is None:
                return
            path.append(root.val)
            k -= root.val
            if k == 0 and root.left is None and root.right is None:
                res.append(list(path))
            dfs(root.left, path, k)
            dfs(root.right, path, k)
            path.pop()

        dfs(root, [], targetSum)
        return len(res) != 0


