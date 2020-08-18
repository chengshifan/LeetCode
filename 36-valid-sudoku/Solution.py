from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            records = {}
            for num in row:
                if num not in records:
                    records[num] = 1
                else:
                    records[num] = records[num] + 1
            for k, v in records.items():
                if v > 1 and k != '.':
                    return False

        for j in range(0, 9):
            records = {}
            for i in range(0, 9):
                if board[i][j] not in records:
                    records[board[i][j]] = 1
                else:
                    records[board[i][j]] = records[board[i][j]] + 1
            for k, v in records.items():
                if v > 1 and k != '.':
                    return False

        def helper(start_col, end_col, start_row, end_row) -> bool:
            records = {}
            for i in range(start_row, end_row):
                for j in range(start_col, end_col):
                    if board[i][j] not in records:
                        records[board[i][j]] = 1
                    else:
                        records[board[i][j]] = records[board[i][j]] + 1
            for k, v in records.items():
                if v > 1 and k != '.':
                    return False
            return True

        return helper(0, 3, 0, 3) and helper(3, 6, 0, 3) and helper(6, 9, 0, 3) and \
               helper(0, 3, 3, 6) and helper(3, 6, 3, 6) and helper(6, 9, 3, 6) and \
               helper(0, 3, 6, 9) and helper(3, 6, 6, 9) and helper(6, 9, 6, 9)
