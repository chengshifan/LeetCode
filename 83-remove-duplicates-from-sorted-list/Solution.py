# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        if p is None or p.next is None:
            return head
        checks = [p.val]
        while p is not None and p.next is not None:
            if p.next.val in checks:
                p.next = p.next.next
                continue
            else:
                checks.append(p.next.val)
                p = p.next
        return head
