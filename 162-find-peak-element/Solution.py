from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        n = len(nums)
        if n == 1:
            return 0
        if nums[1] < nums[0]:
            return 0
        if nums[n - 2] < nums[n - 1]:
            return n - 1

        def helper(nums, start, end) -> int:
            mid = (start + end) // 2
            left, right = mid - 1, mid + 1
            if left >= 0 and right <= n - 1:
                if nums[left] < nums[mid] > nums[right]:
                    return mid
                elif nums[left] > nums[mid] > nums[right]:
                    return helper(nums, 0, mid)
                else:
                    return helper(nums, mid, end)

        return helper(nums, 0, n)

