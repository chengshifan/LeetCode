from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [['0' for _ in range(n)]]
        while len(res) < pow(2, n):
            datas = res[-1][:]
            for i in range(len(datas)):
                if datas[i] == '0':
                    datas[i] = '1'
                    if datas not in res:
                        res.append(datas)
                        break
                    else:
                        datas[i] = '0'
                else:
                    datas[i] = '0'
                    if datas not in res:
                        res.append(datas)
                        break
                    else:
                        datas[i] = '1'

        return [int("".join(re), 2) for re in res]