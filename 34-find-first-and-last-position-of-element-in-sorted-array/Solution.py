from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums or nums[0] > target or nums[-1] < target:
            return res
        start = 0
        end = len(nums) - 1
        end_ok = False
        start_ok = False
        while start <= end:
            if start_ok and end_ok or nums[start] > target or nums[end] < target:
                break
            if nums[end] == target:
                end_ok = True
                res[1] = end if res[1] == -1 or res[1] < end else res[1]
            if nums[start] == target:
                start_ok = True
                res[0] = start if res[0] == -1 or res[0] > start else res[0]
            if not start_ok and nums[start] < target:
                start += 1
            if not end_ok and nums[end] > target:
                end -= 1

        return res
