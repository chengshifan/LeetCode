from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = [num for num in set(nums)]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                if nums[mid] < nums[l] <= target:
                    r = mid - 1
                else:
                    l = mid + 1
            if nums[mid] > target:
                if target <= nums[r] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
