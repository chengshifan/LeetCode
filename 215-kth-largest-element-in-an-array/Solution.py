from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        n = len(nums)
        if n < k:
            return None
        k_nums = [nums[i] for i in range(0, k)]
        for i in range(k, n):
            min_k_num = min(k_nums)
            if min_k_num < nums[i]:
                k_nums.remove(min_k_num)
                k_nums.append(nums[i])
        return min(k_nums)
