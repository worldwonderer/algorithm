
# @Title: 反转链表 (Reverse Linked List)
# @Author: 18015528893
# @Date: 2021-01-07 19:34:33
# @Runtime: 44 ms
# @Memory: 19.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

