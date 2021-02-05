
# @Title: 分隔链表 (Split Linked List in Parts)
# @Author: 18015528893
# @Date: 2021-02-05 11:04:17
# @Runtime: 52 ms
# @Memory: 15.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if root is None:
            return [None for _ in range(k)]

        length = self.get_length(root)
        a = length // k
        cut_count_arr = [a] * k
        b = length % k
        for i in range(b):
            cut_count_arr[i] += 1
        print(cut_count_arr)

        cur = root
        res = []
        for cut_count in cut_count_arr:
            left = cur
            cur = self.cut(cur, cut_count)
            res.append(left)
        return res

    def get_length(self, head):
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        return length

    def cut(self, head, n):
        p = head
        while n - 1 > 0 and p:
            p = p.next
            n -= 1
        if p is None:
            return
        remain = p.next
        p.next = None
        return remain


