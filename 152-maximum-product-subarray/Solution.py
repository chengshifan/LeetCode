from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        begin, target = nums[0], 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                continue
            else:
                target = i
                break
        return min(nums[target], nums[0])


print(Solution().findMin([1, 1, 1, 1]))
