
# @Title: 从上到下打印二叉树 II (从上到下打印二叉树 II LCOF)
# @Author: 18015528893
# @Date: 2021-01-20 21:40:45
# @Runtime: 48 ms
# @Memory: 15.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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


