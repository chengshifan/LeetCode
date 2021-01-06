# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd_head, even_head = head, head.next
        p, q = odd_head, even_head
        while p and p.next and p.next.next:
            p.next = p.next.next
            p = p.next
            if q and q.next and q.next.next:
                q.next = q.next.next
                q = q.next

        if q:
            q.next = None
        if p:
            p.next = even_head

        return odd_head
