
# @Title: 两数相加 II (Add Two Numbers II)
# @Author: 18015528893
# @Date: 2021-02-04 22:41:36
# @Runtime: 80 ms
# @Memory: 14.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while s1 or s2 or carry != 0:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            total = a + b + carry
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            node = ListNode(total, head)
            head = node
        return head


