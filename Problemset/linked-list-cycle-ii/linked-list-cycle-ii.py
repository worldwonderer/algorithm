
# @Title: 环形链表 II (Linked List Cycle II)
# @Author: 18015528893
# @Date: 2021-02-12 21:48:37
# @Runtime: 56 ms
# @Memory: 17.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return 
        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                break
        if f is None or f.next is None:
            return
        
        f = head
        while f != s:
            f = f.next
            s = s.next
        return f
        
