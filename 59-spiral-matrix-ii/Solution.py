from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        paths = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        i = j = 0
        cur = 1

        def helper(x, y, cur, res, visited, path, paths):
            if x >= n or x < 0 or y >= n or y < 0 or visited[x][y]:
                return
            res[x][y] = cur
            visited[x][y] = True
            if path:
                helper(x + path[0], y + path[1], cur + 1, res, visited, path, paths)
            for path in paths:
                helper(x + path[0], y + path[1], cur + 1, res, visited, path, paths)

        helper(i, j, cur, res, visited, None, paths)
        return res
