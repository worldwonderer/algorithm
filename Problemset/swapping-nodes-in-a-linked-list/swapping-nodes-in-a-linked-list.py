
# @Title: 交换链表中的节点 (Swapping Nodes in a Linked List)
# @Author: 18015528893
# @Date: 2021-02-04 22:47:44
# @Runtime: 892 ms
# @Memory: 48.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        f = s = head
        for _ in range(k-1):
            f = f.next
        p = f
        f = f.next
        while f:
            f = f.next
            s = s.next
        p.val, s.val = s.val, p.val
        return head


