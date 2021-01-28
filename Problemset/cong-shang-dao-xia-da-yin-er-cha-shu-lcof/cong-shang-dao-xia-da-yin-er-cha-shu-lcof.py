
# @Title: 从上到下打印二叉树 (从上到下打印二叉树 LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 21:36:46
# @Runtime: 44 ms
# @Memory: 14.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return res


