
# @Title: 返回倒数第 k 个节点 (Kth Node From End of List LCCI)
# @Author: 18015528893
# @Date: 2021-02-13 10:46:32
# @Runtime: 44 ms
# @Memory: 14.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        f = s = head
        for _ in range(k):
            f = f.next
        while f:
            f = f.next
            s = s.next
        return s.val

