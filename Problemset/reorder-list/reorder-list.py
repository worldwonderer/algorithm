
# @Title: 重排链表 (Reorder List)
# @Author: 18015528893
# @Date: 2021-02-04 15:38:09
# @Runtime: 104 ms
# @Memory: 23.7 MB

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
        if head is None:
            return
        if head.next is None:
            return

        slow = head
        fast = head.next  # 如果是fast=head，那么对于长度为偶数的链表是落在后中点，如果是fast=head.next则落在前中点

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        q = self.reverse(slow.next)
        slow.next = None
        p = head

        while p.next:
            tmp = p.next
            p.next = q
            q = q.next
            p.next.next = tmp
            p = p.next.next
        if q:
            p.next = q
        return

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            next_tmp = cur.next
            cur.next = pre
            pre = cur
            cur = next_tmp
        return pre


