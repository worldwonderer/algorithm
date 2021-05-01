
# @Title: 反转链表 (Reverse Linked List)
# @Author: 18015528893
# @Date: 2021-02-18 20:14:53
# @Runtime: 36 ms
# @Memory: 15.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

