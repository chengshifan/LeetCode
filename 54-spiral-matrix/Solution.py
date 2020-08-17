from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False] * n for i in range(m)]
        if m == 0:
            return matrix[0]
        up = [-1, 0]
        down = [1, 0]
        right = [0, 1]
        left = [0, -1]
        res = []
        directs = [right, down, left, up]
        i = j = k = 0
        while False in [y for x in visited for y in x]:
            res.append(matrix[i][j])
            visited[i][j] = True
            next_i = i + directs[k][0]
            next_j = j + directs[k][1]
            if 0 <= next_i < m and 0 <= next_j < n and not visited[next_i][next_j]:
                i, j = next_i, next_j
            else:
                k = (k + 1) % 4
                next_i = i + directs[k][0]
                next_j = j + directs[k][1]
                i, j = next_i, next_j

        return res