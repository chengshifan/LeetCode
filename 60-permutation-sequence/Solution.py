class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]

        def helper1(n_temp):
            if n_temp == 1:
                return 1
            return n_temp * helper1(n_temp - 1)

        total = helper1(n)
        each = total // n
        begin = 1
        while k > each:
            k = k - each
            begin += 1

        res = []
        def helper(cur, datas):
            if not datas:
                res.append(cur[:])
                return
            for data in datas[:]:
                datas.remove(data)
                cur.append(data)
                helper(cur, datas)
                cur.remove(data)
                datas.append(data)

        nums.remove(begin)
        helper([], nums)
        result = [str(begin)]+[str(i) for i in sorted(res)[k-1]]
        return "".join(result)