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
