    # Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        datas = [i for i in range(1, n + 1)]
        if not datas:
            return []

        def buildTrees(datas):
            __res = []
            if not datas:
                return [None]
            for i in range(len(datas)):
                left_trees = buildTrees(datas[0:i])
                right_trees = buildTrees(datas[i + 1:])
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(datas[i])
                        root.left = l
                        root.right = r
                        __res.append(root)
            return __res

        res = buildTrees(datas)
        return res
