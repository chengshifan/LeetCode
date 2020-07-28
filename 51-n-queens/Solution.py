from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n <= 3:
            return []
        datas = [['.' for _ in range(n)] for _ in range(n)]

        def backTrace(paths, datas, cur, n, invalid):
            if cur >= n:
                return
            for j in range(n):
                if (cur, j) not in invalid:
                    datas[cur][j] = 'Q'
                    if cur == n - 1:
                        path = []
                        for data in datas:
                            path.append(''.join(data))
                        paths.append(path)
                        datas[cur][j] = '.'
                        return
                    invalid_this_turn = []
                    invalid_this_turn += [(cur, j)]
                    invalid_this_turn += [(cur, x) for x in range(j + 1, n)]
                    invalid_this_turn += [(cur, x) for x in range(j - 1, -1, -1)]
                    invalid_this_turn += [(y, j) for y in range(cur + 1, n)]
                    invalid_this_turn += [(y, j) for y in range(cur - 1, -1, -1)]
                    x, y = cur + 1, j + 1
                    while x < n and y < n:
                        invalid_this_turn += [(x, y)]
                        x += 1
                        y += 1
                    x, y = cur - 1, j - 1
                    while x >= 0 and y >= 0:
                        invalid_this_turn += [(x, y)]
                        x -= 1
                        y -= 1
                    x, y = cur + 1, j - 1
                    while x < n and y >= 0:
                        invalid_this_turn += [(x, y)]
                        x += 1
                        y -= 1
                    x, y = cur - 1, j + 1
                    while x >= 0 and y < n:
                        invalid_this_turn += [(x, y)]
                        x -= 1
                        y += 1
                    invalid += invalid_this_turn
                    backTrace(res, datas, cur + 1, n, invalid)
                    datas[cur][j] = '.'
                    [invalid.pop() for _ in range(len(invalid_this_turn))]
        res = []
        backTrace(res, datas, 0, n, [])
        return res
