
# @Title: 二叉树的所有路径 (Binary Tree Paths)
# @Author: 18015528893
# @Date: 2021-02-14 17:30:19
# @Runtime: 32 ms
# @Memory: 15 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        
        def dfs(root, path):
            if root is None:
                return

            path.append(root.val)
            if root.left is None and root.right is None:
                result.append('->'.join([str(i) for i in path]))
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
        
        dfs(root, [])
        return result

