
# @Title: 二叉树的层序遍历 (Binary Tree Level Order Traversal)
# @Author: 18015528893
# @Date: 2021-02-14 11:58:01
# @Runtime: 36 ms
# @Memory: 15.1 MB

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
        
        q = deque()
        q.append(root)
        result = []
        while q:
            size = len(q)
            floor = []
            for _ in range(size):
                node = q.popleft()
                floor.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(floor)
        return result

