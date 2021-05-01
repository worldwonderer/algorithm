
# @Title: 链表求和 (Sum Lists LCCI)
# @Author: 18015528893
# @Date: 2021-02-12 21:23:09
# @Runtime: 60 ms
# @Memory: 14.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        carry = 0
        p = dummy
        while l1 or l2 or carry == 1:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            if carry == 1:
                total += 1
                carry = 0
            if total >= 10:
                carry = 1
                total -= 10
            p.next = ListNode(total)
            p = p.next
        return dummy.next

