from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = [[]]
        for num in nums:
            temp_res = [i[:] for i in res]
            for re in temp_res:
                re.append(num)
                res.append(re)
        return res