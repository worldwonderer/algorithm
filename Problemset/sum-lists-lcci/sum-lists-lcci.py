
# @Title: 链表求和 (Sum Lists LCCI)
# @Author: 18015528893
# @Date: 2021-02-04 23:05:37
# @Runtime: 80 ms
# @Memory: 15 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        carry = 0
        while l1 or l2 or carry != 0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            total = a + b + carry
            if total >= 10:
                total -= 10
                carry = 1
            else:
                carry = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            p.next = ListNode(total)
            p = p.next
        return dummy.next


