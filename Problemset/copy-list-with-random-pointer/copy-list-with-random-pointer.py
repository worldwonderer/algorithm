
# @Title: 复制带随机指针的链表 (Copy List with Random Pointer)
# @Author: 18015528893
# @Date: 2021-02-03 16:57:31
# @Runtime: 44 ms
# @Memory: 16 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copied = dict()

        def dfs(head):
            if head is None:
                return
            if head in copied:
                return copied[head]
            node = Node(head.val)
            copied[head] = node
            node.next = dfs(head.next)
            node.random = dfs(head.random)
            return node

        return dfs(head)


