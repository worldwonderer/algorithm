
# @Title: 合并K个升序链表 (Merge k Sorted Lists)
# @Author: 18015528893
# @Date: 2021-02-03 14:44:00
# @Runtime: 84 ms
# @Memory: 18.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))

        dummy = ListNode(0)
        cur = dummy

        while h:
            min_val, i, min_node = heapq.heappop(h)
            cur.next = ListNode(min_val)
            cur = cur.next
            if min_node.next:
                heapq.heappush(h, (min_node.next.val, i, min_node.next))

        return dummy.next


