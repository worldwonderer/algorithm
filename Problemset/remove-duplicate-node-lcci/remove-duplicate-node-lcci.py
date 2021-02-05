
# @Title: 移除重复节点 (Remove Duplicate Node LCCI)
# @Author: 18015528893
# @Date: 2021-02-05 15:09:39
# @Runtime: 68 ms
# @Memory: 20.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        # Python超时
        # if head is None or head.next is None:
        #     return head
        # cur = head
        # while cur:
        #     p = cur
        #     while p.next:
        #         if p.next.val == cur.val:
        #             p.next = p.next.next
        #         else:
        #             p = p.next
        #     cur = cur.next
        # return head
        if head is None:
            return

        visited = {head.val}
        pre = head
        cur = head.next
        while cur:
            if cur.val in visited:
                pre.next = pre.next.next
                cur = pre.next
            else:
                visited.add(cur.val)
                cur = cur.next
                pre = pre.next
        return head


