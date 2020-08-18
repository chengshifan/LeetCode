from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        status = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not status[i][j]:
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                    status[i][j] = True
                    status[j][i] = True

        [matrix[i].reverse() for i in range(n)]