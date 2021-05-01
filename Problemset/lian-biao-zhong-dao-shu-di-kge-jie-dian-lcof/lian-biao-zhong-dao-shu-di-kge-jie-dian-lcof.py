
# @Title: 链表中倒数第k个节点 (链表中倒数第k个节点 LCOF)
# @Author: 18015528893
# @Date: 2021-02-12 17:56:24
# @Runtime: 44 ms
# @Memory: 14.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return
        s = f = head
        for _ in range(k):
            f = f.next
        if f is None:
            return head
        while f.next:
            s = s.next
            f = f.next
        return s.next

