class Solution(object):
    def combinationSum2(self, candidates, target):
        sorted(candidates)
        res = []

        def find(index, nums, temp_sum, temp_res):
            if temp_sum > target or index == len(nums) + 1:
                return
            if temp_sum == target:
                if sorted(temp_res) not in res:
                    res.append(sorted(temp_res[:]))
                return
            for i in range(index, len(nums)):
                temp_res.append(nums[i])
                temp_sum = sum(temp_res)
                temp = nums[:]
                nums.remove(nums[i])
                find(i, nums, temp_sum, temp_res)
                del temp_res[len(temp_res) - 1]
                nums = temp[:]

        find(0, candidates, 0, [])
        return res