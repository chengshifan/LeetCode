from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2 if nums[0] != nums[1] else 1
        dp = [1 for _ in range(n)]
        dp[1] = 2 if nums[0] != nums[1] else 1
        flag = None
        begin = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                flag = True
                begin = i
                break
            elif nums[i] < nums[i - 1]:
                flag = False
                begin = i
                break
            else:
                i += 1
        if flag is None and begin == 0:
            return 1
        for i in range(begin, n):
            if flag:
                if nums[i] > nums[i - 1]:
                    dp[i], flag = dp[i - 1] + 1, not flag
                else:
                    dp[i], flag = dp[i - 1], flag
            else:
                if nums[i] < nums[i - 1]:
                    dp[i], flag = dp[i - 1] + 1, not flag
                else:
                    dp[i], flag = dp[i - 1], flag
        return dp[-1]


print(Solution().wiggleMaxLength([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]))
