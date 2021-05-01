
# @Title: 合并K个升序链表 (Merge k Sorted Lists)
# @Author: 18015528893
# @Date: 2021-02-18 11:34:32
# @Runtime: 80 ms
# @Memory: 17.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode()
        p = dummy
        h = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(h, (head.val, i, head))

        while h:
            _, i, node = heapq.heappop(h)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))

        return dummy.next


