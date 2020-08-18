# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        nums = []
        length = 0
        while p:
            nums.append(p.val)
            length += 1
            p = p.next
        p = head
        target = length - n
        if target == 0:
            return head.next
        count = 0
        while p:
            if count == target - 1:
                p.next = p.next.next
            p = p.next
            count += 1
        return head