class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def helper(nums, p, q):
            if p == q:
                if nums[:] not in res:
                    res.append(nums[:])
                    return
            else:
                for i in range(p, q + 1):
                    nums[i], nums[p] = nums[p], nums[i]
                    helper(nums, p + 1, q)
                    nums[i], nums[p] = nums[p], nums[i]

        helper(nums, 0, len(nums) - 1)
        return res
