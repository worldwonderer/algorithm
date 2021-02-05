
# @Title: 二叉树的层序遍历 (Binary Tree Level Order Traversal)
# @Author: 18015528893
# @Date: 2021-02-05 22:57:04
# @Runtime: 52 ms
# @Memory: 15.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            floor = []
            for _ in range(size):
                node = q.popleft()
                if node:
                    floor.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if floor:
                res.append(floor)
        return res


