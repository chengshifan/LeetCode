class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # This method will throw runtime error but the idea is correct
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        def helper(head: ListNode, node: ListNode) -> ListNode:
            if not node or not node.next:
                return node
            pre = None
            p = node
            while p:
                q = p.next
                p.next = pre
                pre = p
                p = q
            head.next = pre
            helper(pre, pre.next)

        helper(head, head.next)
