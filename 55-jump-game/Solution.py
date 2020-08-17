from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1 or (len(set(nums)) == 1 and list(set(nums)) != [0]):
            return True

        n = len(nums)
        dp = n * [False]
        dp[0] = True
        for i in range(1, n):
            for j in range(0, i):
                if dp[j] and i - j <= nums[j]:
                    dp[i] = True
                    break
        return dp[n - 1]