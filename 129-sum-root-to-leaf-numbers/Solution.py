# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return root.val
        paths = []

        def helper(node: TreeNode, path: []):
            path.append(str(node.val))
            if node.left is None and node.right is None:
                paths.append(int(''.join(path)))

            if node.left is not None:
                helper(node.left, path)

            if node.right is not None:
                helper(node.right, path)
            del path[-1]
            return

        helper(root, [])
        return sum(paths)
