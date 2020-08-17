from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1 and len(nums) - i > 2:
            if nums[i] != nums[i + 1]:
                i = i + 1
            else:
                while i < len(nums) - 2:
                    if nums[i + 2] == nums[i]:
                        del nums[i + 2]
                    else:
                        i = i + 2
                        break
        return len(nums)