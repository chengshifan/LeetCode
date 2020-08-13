# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        p = head.next
        start = head
        end = head
        while p:
            if p.val >= end.val:
                end.next = p
                end = p
                p = end.next
            elif p.val <= start.val:
                end.next = p.next
                p.next = start
                start = p
                p = end.next
            else:
                left = start
                right = end
                while left != right:
                    smaller = left.val
                    larger = left.next.val
                    if smaller < p.val <= larger:
                        end.next = p.next
                        temp = left.next
                        left.next = p
                        p.next = temp
                        break
                    else:
                        left = left.next
                p = end.next

        return start
