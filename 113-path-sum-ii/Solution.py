# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return res

        def helper(treeNode: TreeNode, target, nums):
            if treeNode is None:
                return
            if treeNode.right is None and treeNode.left is None and treeNode.val == target:
                nums += [treeNode.val]
                res.append(nums)
                return

            helper(treeNode.left, target - treeNode.val, nums + [treeNode.val])
            helper(treeNode.right, target - treeNode.val, nums + [treeNode.val])

        helper(root, sum, [])
        return res
