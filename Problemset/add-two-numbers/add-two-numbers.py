
# @Title: 两数相加 (Add Two Numbers)
# @Author: 18015528893
# @Date: 2021-02-17 18:10:36
# @Runtime: 68 ms
# @Memory: 14.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        carry = 0
        while l1 or l2 or carry == 1:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            if carry == 1:
                total += carry
                carry = 0
            if total >= 10:
                total -= 10
                carry = 1
            p.next = ListNode(total)
            p = p.next
        return dummy.next

