
# @Title: 从尾到头打印链表 (从尾到头打印链表 LCOF)
# @Author: 18015528893
# @Date: 2020-09-15 22:22:05
# @Runtime: 40 ms
# @Memory: 14.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        r = list()
        while head:
            r.append(head.val)
            head = head.next
        return r[::-1]

