from typing import List


class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) <= 0:
            return False
        visited = [[False] * len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.helper(i, j, visited, board, word[1:]):
                        return True
                    else:
                        visited[i][j] = False
        return False

    def helper(self, i, j, visited, board, word):
        if len(word) == 0:
            return True
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            if 0 <= cur_i < len(board) and 0 <= cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                if visited[cur_i][cur_j]:
                    continue
                else:
                    visited[cur_i][cur_j] = True
                    if self.helper(cur_i, cur_j, visited, board, word[1:]):
                        return True
                    else:
                        visited[cur_i][cur_j] = False
        return False