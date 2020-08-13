# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = {}

        def inOrderTraverse(root, level, res):
            if not root:
                return
            if res.get(level):
                temp = res.get(level)
                temp.append(root.val)
                res[level] = temp
            else:
                res[level] = [root.val]
            inOrderTraverse(root.left, level + 1, res)
            inOrderTraverse(root.right, level + 1, res)

        inOrderTraverse(root, 0, res)
        results = []
        for _, v in res.items():
            results.append(v)
        return results
