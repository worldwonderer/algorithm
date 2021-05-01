
# @Title: 反转链表 (反转链表 LCOF)
# @Author: 18015528893
# @Date: 2021-02-28 16:24:33
# @Runtime: 48 ms
# @Memory: 15.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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

