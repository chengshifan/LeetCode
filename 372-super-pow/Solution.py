from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b or len(b) == 0:
            return 1
        tmp = b[-1]

        def helper(num: int, c: int):
            if c == 0:
                return 1
            num %= 1337
            res = 1
            for i in range(c):
                res *= num
                res %= 1337
            return res

        part_1 = helper(a, tmp)
        part_2 = helper(self.superPow(a, b[0:-1]), 10)
        return (part_1 * part_2) % 1337

