from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input:
            return []
        if '+' not in input and '-' not in input and '*' not in input:
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] == '-' or input[i] == '+' or input[i] == '*':
                l_res = self.diffWaysToCompute(input[0:i])
                r_res = self.diffWaysToCompute(input[i + 1:])
                for l_re in l_res:
                    for r_re in r_res:
                        if input[i] == '-':
                            res.append(l_re - r_re)
                        elif input[i] == '+':
                            res.append(l_re + r_re)
                        elif input[i] == '*':
                            res.append(l_re * r_re)
        return res
