from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        count_0 = count_1 = count_2 = 0
        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            elif num == 2:
                count_2 += 1

        j = 0
        for i in range(count_0):
            nums[j] = 0
            j += 1
        for i in range(count_1):
            nums[j] = 1
            j += 1
        for i in range(count_2):
            nums[j] = 2
            j += 1
