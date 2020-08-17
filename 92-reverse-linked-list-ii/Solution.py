# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n == 1:
            return head
        p = head
        start_count = 0
        end_count = 0
        before_start = None
        start = None
        start_flag = False
        while p:
            start_count += 1
            if not start_flag:
                if start_count == m:
                    start = p
                    start_flag = True
                else:
                    before_start = p

            end_count += 1
            if end_count == n:
                end = p
                if m == 1:
                    head = end
                after_end = p.next
                start_record = start
                before_start_record = before_start
                while start and start != after_end:
                    r = before_start
                    q = start.next
                    start.next = r
                    before_start = start
                    start = q
                if before_start_record:
                    before_start_record.next = end
                start_record.next = after_end
                break
            p = p.next

        return head
