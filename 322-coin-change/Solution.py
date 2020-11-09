from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0:
            return 0

        dp = [1000000] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if coin <= i and dp[i - coin] < dp[i]:
                    dp[i] = dp[i - coin] + 1

        return dp[amount] if dp[amount] != 1000000 else -1
