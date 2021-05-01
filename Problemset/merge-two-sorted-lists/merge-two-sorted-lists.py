
# @Title: 合并两个有序链表 (Merge Two Sorted Lists)
# @Author: 18015528893
# @Date: 2021-02-18 11:16:48
# @Runtime: 44 ms
# @Memory: 14.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next


