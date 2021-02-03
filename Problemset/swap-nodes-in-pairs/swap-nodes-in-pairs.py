
# @Title: 两两交换链表中的节点 (Swap Nodes in Pairs)
# @Author: 18015528893
# @Date: 2021-02-03 15:02:57
# @Runtime: 40 ms
# @Memory: 14.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return
        if head.next is None:
            return head
        a = head
        b = head.next.next if head.next else head

        new_head = self.reverse(a, b)
        a.next = self.swapPairs(b)
        return new_head

    def reverse(self, a, b):
        pre = None
        cur = a
        while cur != b:
            next_tmp = cur.next
            cur.next = pre
            pre = cur
            cur = next_tmp
        return pre


