# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        while len(lists) > 1:
            p_0 = lists[0]
            p_1 = lists[1]
            lists.remove(p_0)
            lists.remove(p_1)
            head = ListNode(-1)
            p = head
            while p_0 and p_1:
                if p_0.val <= p_1.val:
                    p.next = p_0
                    p_0 = p_0.next
                else:
                    p.next = p_1
                    p_1 = p_1.next
                p = p.next
            if p_0:
                p.next = p_0
            if p_1:
                p.next = p_1
            lists.append(head.next)

        return lists[0]
