class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_num = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if abs(nums[i] + nums[l] + nums[r] - target) < abs(closest_num - target):
                    closest_num = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] > target:
                    r = r - 1
                else:
                    l = l + 1

        return closest_num
