from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words or len(words) == 1:
            return 0
        n = len(words)
        dp = [[0] * n for _ in range(n)]
        ans = 0

        def helper(str_a: str, str_b: str) -> bool:
            if str_a in str_b or str_a in str_b:
                return True
            res = False
            for char in str_a:
                if char in str_b:
                    res = True
                    break
            return res

        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    dp[i][j] = 0
                elif i > j:
                    dp[i][j] = dp[j][i]
                else:
                    dp[i][j] = len(words[i]) * len(words[j]) if not helper(words[i], words[j]) else 0
                if dp[i][j] > ans:
                    ans = dp[i][j]
        return ans