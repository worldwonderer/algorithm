
# @Title: 复杂链表的复制 (复杂链表的复制  LCOF)
# @Author: 18015528893
# @Date: 2021-02-13 15:41:01
# @Runtime: 44 ms
# @Memory: 15.6 MB

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
        if head is None:
            return

        cur = head 
        while cur:
            copied = Node(cur.val)
            copied.next = cur.next
            cur.next = copied
            cur = cur.next.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        copied_cur = head.next
        copied_head = head.next
        while cur:
            cur.next = cur.next.next
            cur = cur.next
            if copied_cur.next:
                copied_cur.next = copied_cur.next.next
                copied_cur = copied_cur.next
        return copied_head
        
