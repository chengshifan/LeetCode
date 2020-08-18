import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if int(dividend / divisor) < -math.pow(2, 31) or int(dividend / divisor) > math.pow(2, 31) - 1:
            return int(math.pow(2, 31)) - 1
        else:
            return int(dividend / divisor)