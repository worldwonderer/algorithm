
# @Title: 路径总和 III (Path Sum III)
# @Author: 18015528893
# @Date: 2021-02-08 12:46:49
# @Runtime: 756 ms
# @Memory: 16 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    ret = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return self.ret

        self.helper(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.ret

    def helper(self, root, s):
        def dfs(root, s):
            if root is None:
                return
            s -= root.val
            if s == 0:
                self.ret += 1
            dfs(root.left, s)
            dfs(root.right, s)

        dfs(root, s)



        

