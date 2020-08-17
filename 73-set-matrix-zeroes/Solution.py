from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_indexs = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_indexs.append([i, j])

        for index in zero_indexs:
            for j in range(n):
                matrix[index[0]][j] = 0
            for i in range(m):
                matrix[i][index[1]] = 0