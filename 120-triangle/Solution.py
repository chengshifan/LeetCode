import sys
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        dp = [[sys.maxsize for _ in range(0, n)] for _ in range(0, n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(0, i + 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + triangle[i][j])
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + triangle[i][j]) if j - 1 >= 0 else dp[i][j]
        return min(dp[n - 1])
