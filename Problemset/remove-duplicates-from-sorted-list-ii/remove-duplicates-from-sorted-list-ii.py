
# @Title: 删除排序链表中的重复元素 II (Remove Duplicates from Sorted List II)
# @Author: 18015528893
# @Date: 2021-02-03 17:17:29
# @Runtime: 48 ms
# @Memory: 14.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                tmp = cur.next
                val = tmp.val
                while tmp and tmp.val == val:
                    tmp = tmp.next
                cur.next = tmp
            else:
                cur = cur.next
        return dummy.next


