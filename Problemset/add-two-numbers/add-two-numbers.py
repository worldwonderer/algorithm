
# @Title: 两数相加 (Add Two Numbers)
# @Author: 18015528893
# @Date: 2021-02-02 23:41:45
# @Runtime: 68 ms
# @Memory: 14.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cursor = dummy
        carry = 0
        while l1 or l2 or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0
            cursor.next = ListNode(s)
            cursor = cursor.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


