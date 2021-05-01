
# @Title: 两数相加 II (Add Two Numbers II)
# @Author: 18015528893
# @Date: 2021-02-13 12:48:25
# @Runtime: 72 ms
# @Memory: 14.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
    
        s2 = []
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None
        while s1 or s2 or carry == 1:
            total = 0
            total += s1.pop() if s1 else 0
            total += s2.pop() if s2 else 0
            if carry == 1:
                total += 1
                carry = 0
            if total >= 10:
                carry = 1
                total -= 10
            node = ListNode(total)
            node.next = head
            head = node
        return head

