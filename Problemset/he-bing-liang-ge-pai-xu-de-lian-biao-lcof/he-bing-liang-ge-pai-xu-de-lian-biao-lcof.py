
# @Title: 合并两个排序的链表 (合并两个排序的链表  LCOF)
# @Author: 18015528893
# @Date: 2021-01-17 22:49:01
# @Runtime: 68 ms
# @Memory: 15.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next

