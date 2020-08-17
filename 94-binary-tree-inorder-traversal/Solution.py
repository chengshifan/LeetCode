# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helpler(root):
            if not root:
                return
            helpler(root.left)
            res.append(root.val)
            helpler(root.right)

        helpler(root)
        return res
