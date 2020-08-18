from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] < target:
                start += 1
                continue
            if nums[start] == target:
                return start
            if nums[end] > target:
                end -= 1
                continue
            if nums[end] == target:
                return end
            break
        return -1
