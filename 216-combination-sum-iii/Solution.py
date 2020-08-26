from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        min_sum = sum(nums[0:k])
        res = []

        def backTrace(cur, nums):
            if sum(cur) == n and len(cur) == k:
                res.append(cur[:])
                return
            if not nums or len(cur) == k:
                return
            for num in nums[:]:
                nums.remove(num)
                cur.append(num)
                if sorted(cur) == cur:
                    backTrace(cur, nums)
                cur.remove(num)
                nums.append(num)

        if n < min_sum:
            return [[]]
        elif n == min_sum:
            return [nums[0:k]]
        else:
            backTrace([], nums)

        return res


