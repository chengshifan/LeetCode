from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        left = right = 0
        if len(nums) % 2 == 0:
            right = len(nums) / 2
            left = right - 1
        else:
            right = left = len(nums) // 2

        return (nums[int(left)] + nums[int(right)]) / 2
