from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        def helper(n):
            return n[1] == 2
        from collections import Counter
        return list(map(lambda x: x[0], list(filter(helper, Counter(nums).items()))))
