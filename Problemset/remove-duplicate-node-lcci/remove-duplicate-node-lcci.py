
# @Title: 移除重复节点 (Remove Duplicate Node LCCI)
# @Author: 18015528893
# @Date: 2021-02-13 15:43:59
# @Runtime: 68 ms
# @Memory: 20.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        pre = head
        cur = head.next
        s = {pre.val}
        while cur:
            if cur.val in s:
                pre.next = pre.next.next
            else:
                pre = pre.next
                s.add(cur.val)
            cur = pre.next
        return head

