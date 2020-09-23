class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def helper(start, end, nums, target):
            if start > end:
                return False
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                return helper(start, mid - 1, nums, target)
            else:
                return helper(mid + 1, end, nums, target)

        for nums in matrix:
            if nums and nums[0] <= target <= nums[-1]:
                if helper(0, len(nums) - 1, nums, target):
                    return True
        return False
