class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        if x == 1:
            return 1

        def func(x: float, n: int) -> float:
            if n < 2:
                return x
            elif n == 2:
                return x * x
            else:
                if n % 2 == 0:
                    return func(func(x, int(n / 2)), 2)
                else:
                    return func(func(x, int(n / 2)), 2) * x

        res = func(x, abs(n))
        if n > 0:
            return res
        else:
            return 1 / res
