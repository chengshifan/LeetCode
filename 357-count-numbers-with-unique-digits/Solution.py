class Solution:
    cnt = 0

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def helper(num, n):
            if len((set(num))) != len(num):
                # print(num)
                self.cnt += pow(10, n)
                return
            if n > 0:
                for i in range(0, 10):
                    helper(num + str(i), n - 1)

        for j in range(n, 0, -1):
            for i in range(1, 10):
                helper(str(i), j - 1)
        return pow(10, n) - self.cnt

