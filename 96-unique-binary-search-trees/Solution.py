# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for j in range(2, n + 1):
            for i in range(1, j + 1):
                dp[j] += dp[i - 1] * dp[j - i]
        return dp[n]
