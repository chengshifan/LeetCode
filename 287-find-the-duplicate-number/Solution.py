from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start, end = 1, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                start = mid + 1
            else:
                end = mid
        return start
