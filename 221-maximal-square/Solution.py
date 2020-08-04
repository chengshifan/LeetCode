from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if int(matrix[i][j]) == 1:
                    row_max = int(dp[i - 1][j]) if i - 1 >= 0 else 0
                    col_max = int(dp[i][j - 1]) if j - 1 >= 0 else 0
                    x, y, z = i + 1, j + 1, 1
                    while x < m and y < n:
                        sub_matrix = [int(matrix[p][q]) for p in range(i, x + 1) for q in range(j, y + 1)]
                        if not sub_matrix or 0 in sub_matrix:
                            break
                        else:
                            x += 1
                            y += 1
                            z += 1
                    dp[i][j] = max(row_max, col_max, 1, z)

        return pow(max(map(max, dp)), 2)
