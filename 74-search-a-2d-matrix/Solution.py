from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            if not nums:
                continue
            if nums[-1] < target:
                continue
            else:
                return target in nums
        return False
