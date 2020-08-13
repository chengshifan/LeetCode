# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        n = len(preorder)
        if n == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        mid = 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                mid = i
                break
        left_preorder = preorder[1:mid + 1]
        right_preorder = preorder[mid + 1: n]
        left_inorder = inorder[0:mid]
        right_inorder = inorder[mid + 1:n]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
