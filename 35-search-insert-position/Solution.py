from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        try:
            return nums.index(target)
        except ValueError as ex:
            if nums[0] > target:
                return 0
            elif nums[-1] < target:
                return len(nums)
            else:
                for i in range(0, len(nums) - 1):
                    if nums[i] < target < nums[i + 1]:
                        return i + 1
