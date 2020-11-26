from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num not in res:
                res.append(num)
            else:
                res.remove(num)
        return res

print(Solution().singleNumber([1,2,1,3,2,5]))