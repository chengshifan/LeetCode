class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        left, slow, fast = head.next, head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        right = slow.next
        slow.next = None
        p = right
        pre = None
        while p:
            q = p.next
            p.next = pre
            pre = p
            p = q
        right = pre
        use_left = False
        p = head
        while left and right:
            if use_left:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
            use_left = not use_left
        if left:
            p.next = left
        if right:
            p.next = right
