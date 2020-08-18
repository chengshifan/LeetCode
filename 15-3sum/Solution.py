from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            begin = i + 1
            end = len(nums) - 1
            while begin < end:
                sum = nums[i] + nums[begin] + nums[end]
                if sum == 0:
                    res.append([nums[i], nums[begin], nums[end]])
                    while begin < end and nums[begin] == nums[begin + 1]:
                        begin = begin + 1
                    while begin < end and nums[end] == nums[end - 1]:
                        end = end - 1
                    begin = begin + 1
                    end = end - 1
                elif sum > 0:
                    end = end - 1
                elif sum < 0:
                    begin = begin + 1

        return res
