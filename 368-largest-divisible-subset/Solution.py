from typing import List


class Solution(object):
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        dp = [[num] for num in nums]
        max_seq = []
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + nums[i:i + 1]
            if len(dp[i]) > len(max_seq):
                max_seq = dp[i]
        return max_seq
