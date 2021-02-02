
# @Title: 反转链表 (Reverse Linked List)
# @Author: 18015528893
# @Date: 2021-02-02 22:14:39
# @Runtime: 48 ms
# @Memory: 19.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        pre = None
        cur = head
        while cur:
            next_tmp = cur.next
            cur.next = pre
            pre = cur
            cur = next_tmp
        return pre

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

