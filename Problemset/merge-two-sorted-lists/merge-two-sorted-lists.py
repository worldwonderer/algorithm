
# @Title: 合并两个有序链表 (Merge Two Sorted Lists)
# @Author: 18015528893
# @Date: 2019-10-21 22:27:34
# @Runtime: 48 ms
# @Memory: 13.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        q = head
        while True:
            if l1 is not None and l2 is not None:
                if l1.val > l2.val:
                    q.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    q.next = ListNode(l1.val)
                    l1 = l1.next
            elif l1 is not None and l2 is None:
                q.next = ListNode(l1.val)
                l1 = l1.next
            elif l2 is not None and l1 is None:
                q.next = ListNode(l2.val)
                l2 = l2.next
            elif l1 is None and l2 is None:
                break
            q = q.next
        return head.next
                
                
            
