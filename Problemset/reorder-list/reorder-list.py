
# @Title: 重排链表 (Reorder List)
# @Author: 18015528893
# @Date: 2021-02-12 16:05:36
# @Runtime: 100 ms
# @Memory: 23.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        
        s = head
        f = head.next
        
        while f and f.next:
            f = f.next.next
            s = s.next
        
        l2 = s.next
        def reverse(head):
            pre = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        
        l2 = reverse(l2)
        s.next = None
        l1 = head
        while l2:
            tmp = l1.next
            l1.next = l2
            l2 = l2.next
            l1 = l1.next
            l1.next = tmp
            l1 = l1.next

