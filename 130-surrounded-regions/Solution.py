from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        starts = []
        for i in range(0, rows):
            if board[i][0] == 'O':
                starts.append((i, 0))
            if board[i][cols - 1] == 'O':
                starts.append((i, cols - 1))
        for j in range(0, cols):
            if board[0][j] == 'O':
                starts.append((0, j))
            if board[rows - 1][j] == 'O':
                starts.append((rows - 1, j))
        starts = list(set(starts))
        status = [[True for _ in range(0, cols)] for _ in range(0, rows)]
        visited = [[False for _ in range(0, cols)] for _ in range(0, rows)]

        def helper(x, y, rows, cols, status, visited):
            if visited[x][y]:
                return
            visited[x][y] = True
            if status[x][y] is False and x != 0 and y != 0 and x != rows - 1 and y != cols - 1:
                return
            if board[x][y] == 'O':
                status[x][y] = False
                if x + 1 <= rows - 1 and not visited[x + 1][y]:
                    helper(x + 1, y, rows, cols, status, visited)
                if x - 1 >= 0 and not visited[x - 1][y]:
                    helper(x - 1, y, rows, cols, status, visited)
                if y + 1 <= cols - 1 and not visited[x][y + 1]:
                    helper(x, y + 1, rows, cols, status, visited)
                if y - 1 >= 0 and not visited[x][y - 1]:
                    helper(x, y - 1, rows, cols, status, visited)
                return
            else:
                return

        for start in starts:
            helper(start[0], start[1], rows, cols, status, visited)
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if status[i][j]:
                    board[i][j] = 'X'