
# @Title: 删除排序链表中的重复元素 (Remove Duplicates from Sorted List)
# @Author: 18015528893
# @Date: 2019-10-23 01:09:08
# @Runtime: 56 ms
# @Memory: 13.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        p = head
        q = head.next
        while True:
            if q.val == p.val:
                p.next = q.next
                q = p.next
            else:
                p = p.next
                q = q.next
            if q is None:
                break
        return head
