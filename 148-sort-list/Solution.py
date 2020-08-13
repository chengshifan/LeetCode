# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        right_head = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(right_head)
        res = h = ListNode(-1)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next
