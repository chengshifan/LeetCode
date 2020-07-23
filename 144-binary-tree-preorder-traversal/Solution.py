# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        visited = []
        if not root:
            return []
        stack.append(root)
        visited.append(root)
        res = []
        while stack:
            cur_node = stack.pop()
            if (cur_node.right in visited and cur_node.left in visited) or (
                    not cur_node.left and cur_node.right in visited) or (
                    not cur_node.right and cur_node.left in visited) or (not cur_node.left and not cur_node.right):
                res.append(cur_node.val)
                continue
            first, second, last = None, None, None
            if cur_node.right and cur_node.right not in stack and cur_node.right not in res:
                first = cur_node.right

            if cur_node.left and cur_node.left not in stack and cur_node.left not in res:
                second = cur_node.left
            last = cur_node
            if first:
                stack.append(first)
                visited.append(first)
            if second:
                stack.append(second)
                visited.append(second)
            if last:
                stack.append(last)
                visited.append(last)

        return res
