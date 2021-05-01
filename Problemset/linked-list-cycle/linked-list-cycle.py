
# @Title: 环形链表 (Linked List Cycle)
# @Author: 18015528893
# @Date: 2021-02-12 18:00:15
# @Runtime: 64 ms
# @Memory: 18.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True
        return False
