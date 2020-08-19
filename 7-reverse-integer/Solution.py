class Solution:
    def reverse(self, x: int) -> int:
        data = str(x)
        data_reverse = data[::-1]
        if data_reverse[-1] == '-':
            res = '-' + data_reverse[0:-1]
        else:
            res = data_reverse
        if int(res) > pow(2, 31) - 1 or int(res) < pow(-2, 31):
            return 0
        return int(res)


print(Solution().reverse(1534236469))
