# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder_traverse(root: TreeNode, arr: []):
            if not root:
                return
            inorder_traverse(root.left, arr)
            arr.append(root.val)
            inorder_traverse(root.right, arr)

        res = []
        inorder_traverse(root, res)
        for i in range(0, len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True
