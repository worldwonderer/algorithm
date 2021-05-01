
# @Title: 对链表进行插入排序 (Insertion Sort List)
# @Author: 18015528893
# @Date: 2021-02-13 12:05:06
# @Runtime: 168 ms
# @Memory: 16.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(next=head)
        last_sorted = head
        cur = head.next
        while cur:
            if cur.val > last_sorted.val:
                last_sorted = last_sorted.next
            else:
                pre = dummy
                while pre.next.val < cur.val:
                    pre = pre.next
                last_sorted.next = cur.next
                cur.next = pre.next
                pre.next = cur
            cur = last_sorted.next
        return dummy.next
