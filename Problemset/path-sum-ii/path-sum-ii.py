
# @Title: 路径总和 II (Path Sum II)
# @Author: 18015528893
# @Date: 2021-02-14 17:49:42
# @Runtime: 56 ms
# @Memory: 16.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []

        def dfs(root, path, k):
            if root is None:
                return

            path.append(root.val)
            if root.val == k and root.left is None and root.right is None:
                result.append(list(path))

            dfs(root.left, path, k-root.val)
            dfs(root.right, path, k-root.val)
            path.pop()
        
        dfs(root, [], targetSum)
        return result
            
