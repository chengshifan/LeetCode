# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        count = 0
        p = q = head
        first = True
        while p:
            count += 1
            if count % 2 == 0:
                tail = count - 2
                tmp = p.next
                p.next = q
                q.next = tmp
                if first:
                    first = False
                    head = p
                else:
                    r = head
                    tail_count = 0
                    while tail_count < tail - 1:
                        r = r.next
                        tail_count += 1
                    r.next = p
                p = q.next

            else:
                q = p
                p = p.next
        return head
