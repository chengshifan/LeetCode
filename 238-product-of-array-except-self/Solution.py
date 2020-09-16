from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        if n == 1:
            return [0]
        if n == 2:
            return [nums[1], nums[0]]
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]
        l[0] = 1
        r[-1] = 1
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]
        return [l[i] * r[i] for i in range(n)]