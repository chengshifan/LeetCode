from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num_max, num_min, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            pre_max = max(num_max * nums[i], num_min * nums[i], nums[i])
            pre_min = min(num_max * nums[i], num_min * nums[i], nums[i])
            res = max(pre_max, res)
            num_max = pre_max
            num_min = pre_min
        return res

