# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        r = list()
        while head:
            r.append(head.val)
            head = head.next
        return r[::-1]
