
# @Title: 删除排序链表中的重复元素 (Remove Duplicates from Sorted List)
# @Author: 18015528893
# @Date: 2021-02-12 21:40:23
# @Runtime: 44 ms
# @Memory: 14.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                tmp = cur.next
                val = tmp.val
                while tmp and tmp.val == val:
                    tmp = tmp.next
                cur.next = tmp
            cur = cur.next
        return head

