from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = 0
        for num in nums:
            if nums[flag] != num:
                flag += 1
                nums[flag] = num

        return len(nums) and flag + 1
