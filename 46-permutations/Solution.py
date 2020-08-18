from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, nums):
            if not nums:
                result.append(path[:])
                return
            for num in nums[:]:
                path.append(num)
                nums.remove(num)
                backtrack(path, nums)
                path.remove(num)
                nums.append(num)

        backtrack([], nums)

        return result
