
# @Title: 填充每个节点的下一个右侧节点指针 II (Populating Next Right Pointers in Each Node II)
# @Author: 18015528893
# @Date: 2021-02-07 23:03:41
# @Runtime: 64 ms
# @Memory: 16 MB

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
        if root.left is None and root.right is None:
            return root

        def find_next_right(root):
            while root.next:
                if root.next.left:
                    return root.next.left
                if root.next.right:
                    return root.next.right
                root = root.next

        if root.left:
            if root.right:
                root.left.next = root.right
                root.right.next = find_next_right(root)
            else:
                root.left.next = find_next_right(root)
        else:
            if root.right:
                root.right.next = find_next_right(root)
        self.connect(root.right)
        self.connect(root.left)
        return root

