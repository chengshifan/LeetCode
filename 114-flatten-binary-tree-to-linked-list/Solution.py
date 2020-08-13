# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left is None:
                root = root.right
            else:
                left_tree = root.left
                most_right_in_left_tree = left_tree
                while most_right_in_left_tree.right:
                    most_right_in_left_tree = most_right_in_left_tree.right
                most_right_in_left_tree.right = root.right
                root.left = None
                root.right = left_tree
