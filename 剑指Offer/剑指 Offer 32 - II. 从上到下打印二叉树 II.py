# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            floor = []
            for _ in range(size):
                node = queue.popleft()
                if node:
                    floor.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if floor:
                res.append(floor)
        return res
