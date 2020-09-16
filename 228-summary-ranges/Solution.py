from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = end = 0
        n = len(nums)
        ans = []
        nums.append(nums[-1] + 2)
        for i in range(1, n + 1):
            if nums[i] - nums[i - 1] == 1:
                end = i
            else:
                if start == end:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start]) + "->" + str(nums[end]))
                start, end = i, i
        return ans
