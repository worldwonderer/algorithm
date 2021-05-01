
# @Title: 两两交换链表中的节点 (Swap Nodes in Pairs)
# @Author: 18015528893
# @Date: 2021-02-21 12:35:04
# @Runtime: 40 ms
# @Memory: 14.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return
        a = b = head
        for i in range(2):
            if b is None:
                return head
            b = b.next

        new_head = a.next
        a.next.next = a
        a.next = self.swapPairs(b)
        return new_head


