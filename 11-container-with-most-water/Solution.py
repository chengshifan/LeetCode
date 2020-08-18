from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            b = right - left
            if height[left] < height[right]:
                h = height[left]
                left = left + 1
            else:
                h = height[right]
                right = right - 1
            maxArea = max(b * h, maxArea)
        return maxArea
