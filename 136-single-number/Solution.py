from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums[:]:
            nums.remove(num)
            if num not in nums:
                return num
            else:
                nums.append(num)

        return 0
