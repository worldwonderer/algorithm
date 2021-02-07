
# @Title: 填充每个节点的下一个右侧节点指针 (Populating Next Right Pointers in Each Node)
# @Author: 18015528893
# @Date: 2021-02-06 10:03:00
# @Runtime: 268 ms
# @Memory: 16.4 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return

        def helper(n1, n2):
            if n1 is None or n2 is None:
                return

            n1.next = n2
            helper(n1.left, n1.right)
            helper(n2.left, n2.right)
            helper(n1.right, n2.left)

        helper(root.left, root.right)
        return root

