from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False
        total_num = sum(nums)
        if total_num % 2 == 1:
            return False
        half_num = sum(nums) // 2
        n = len(nums)
        dp = [[False] * (half_num + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        if half_num > nums[0]:
            dp[0][nums[0]] = True

        for i in range(1, n):
            num = nums[i]
            for j in range(1, half_num + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][half_num]


print(Solution().canPartition([9, 5]))
