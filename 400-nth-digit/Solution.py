class Solution:
    def findNthDigit(self, n: int) -> int:
        if 0 < n <= 9:
            return n
        c = 9
        d = 1
        while True:
            n, d, c = n - c * len(str(d)), d * 10, c * 10
            if n < c * len(str(d)):
                index = n // len(str(d))
                m = n - index * len(str(d))
                if m == 0:
                    ans = str(range(d, d + n)[index - 1])[-1]
                else:
                    ans = int(str(range(d, d + n)[index])[m - 1])
                break
        return ans
