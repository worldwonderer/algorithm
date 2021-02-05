
# @Title: 合并两个链表 (Merge In Between Linked Lists)
# @Author: 18015528893
# @Date: 2021-02-05 14:22:03
# @Runtime: 432 ms
# @Memory: 20.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p = q = list1
        for _ in range(a-1):
            p = p.next
        for _ in range(b+1):
            q = q.next
        r = list2
        while r.next:
            r = r.next

        p.next = list2
        r.next = q
        return list1


