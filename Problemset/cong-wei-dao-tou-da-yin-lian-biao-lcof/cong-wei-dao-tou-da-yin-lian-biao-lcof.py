
# @Title: 从尾到头打印链表 (从尾到头打印链表 LCOF)
# @Author: 18015528893
# @Date: 2021-02-13 10:43:11
# @Runtime: 128 ms
# @Memory: 24 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []
        return self.reversePrint(head.next) + [head.val]

