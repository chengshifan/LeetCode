class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        datas = [n]
        while True:
            flag = False
            for data in datas[:]:
                if data >= 5:
                    flag = True
                    datas.remove(data)
                    datas.append(data - 3)
                    datas.append(3)
            if not flag:
                break
        ans = 1
        for an in datas:
            ans *= an
        return ans
