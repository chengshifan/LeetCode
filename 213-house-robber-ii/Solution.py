from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]

        def helper(nums):
            dp_1 = [nums[0] for _ in range(n)]
            dp_2 = [0 for _ in range(n)]
            flag_1 = [True for _ in range(n)]
            flag_2 = [False for _ in range(n)]
            for i in range(1, n):
                if dp_1[i - 1] > dp_2[i - 1]:
                    dp_2[i] = dp_1[i - 1]
                    flag_2[i] = flag_1[i - 1]
                elif dp_1[i - 1] == dp_2[i - 1]:
                    dp_2[i] = dp_1[i - 1]
                    flag_2[i] = flag_1[i - 1] and flag_2[i - 1]
                else:
                    dp_2[i] = dp_2[i - 1]
                    flag_2[i] = flag_2[i - 1]
                dp_1[i] = dp_2[i - 1] + nums[i]
                flag_1[i] = flag_2[i - 1]

            if dp_2[-1] >= dp_1[-1]:
                return max(dp_2)
            else:
                if flag_1[-1]:
                    return max(dp_1[0:-1])
                else:
                    return max(dp_1)

        return max(helper(nums), helper(nums[::-1]))
