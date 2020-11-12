class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def helper(num1: str, num2: str, num_remain: str) -> bool:
            if num1.startswith('0') and len(num1) > 1 or num2.startswith('0') and len(num2) > 1:
                return False
            if not num_remain:
                return True
            if num_remain.startswith(str(int(num1) + int(num2))):
                return helper(num2, str(int(num1) + int(num2)), num_remain[len(str(int(num1) + int(num2))):])
            else:
                return False

        if not num or len(num) < 3:
            return False
        end = 2
        start = 0
        while end < len(num):
            for mid in range(start + 1, end):
                if helper(num[start:mid], num[mid:end], num[end:]):
                    return True
            end += 1

        return False


print(Solution().isAdditiveNumber("1023"))
