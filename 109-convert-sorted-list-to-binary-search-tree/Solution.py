# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head
        pre_slow = None
        while fast != None and fast.next != None:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        pre_slow.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
