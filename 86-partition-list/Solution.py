# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p = head
        head_left = None
        head_right = None
        while p:
            if p.val < x:
                if not head_left:
                    head_left = ListNode(p.val)
                else:
                    p_left = head_left
                    while p_left.next:
                        p_left = p_left.next
                    p_left.next = ListNode(p.val)
            else:
                if not head_right:
                    head_right = ListNode(p.val)
                else:
                    p_right = head_right
                    while p_right.next:
                        p_right = p_right.next
                    p_right.next = ListNode(p.val)
            p = p.next

        if head_left:
            p_left = head_left
            while p_left.next:
                p_left = p_left.next
            p_left.next = head_right
            return head_left
        else:
            return head_right
