
# @Title: 从链表中删去总和值为零的连续节点 (Remove Zero Sum Consecutive Nodes from Linked List)
# @Author: 18015528893
# @Date: 2021-02-05 12:38:31
# @Runtime: 176 ms
# @Memory: 15.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        while cur:
            p = cur
            s = None
            while p and s != 0:
                s = 0 if s is None else s
                s += p.val
                p = p.next
            
            if s == 0:
                pre.next = p
                cur = pre.next
            elif p is None:
                cur = cur.next
                pre = pre.next
        return dummy.next


