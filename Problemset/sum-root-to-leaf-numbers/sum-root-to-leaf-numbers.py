
# @Title: 求根到叶子节点数字之和 (Sum Root to Leaf Numbers)
# @Author: 18015528893
# @Date: 2021-02-07 23:11:26
# @Runtime: 44 ms
# @Memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = 0

    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def dfs(root, k):
            if root is None:
                return
            if k == "0":
                k = str(root.val)
            else:
                k += str(root.val)
            if root.left is None and root.right is None:
                self.s += int(k)
            dfs(root.left, k)
            dfs(root.right, k)

        dfs(root, "0")
        return self.s


