
# @Title: 链表组件 (Linked List Components)
# @Author: 18015528893
# @Date: 2021-02-05 11:28:38
# @Runtime: 88 ms
# @Memory: 19.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        g = set(G)
        ret = 0
        cur = head
        while cur:
            if cur.val in g and (cur.next is None or cur.next.val not in g):
                ret += 1
            cur = cur.next
        return ret
        

