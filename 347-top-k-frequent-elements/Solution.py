from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for item in sorted((Counter(nums).items()), key=lambda x: x[1], reverse=True)[0:k]:
            ans.append(item[0])
        return ans
