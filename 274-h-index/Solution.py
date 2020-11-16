from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        if min(citations) > n:
            return n
        while n >= 0:
            arr_1, arr_2 = [], []
            for citation in citations:
                if citation >= n:
                    arr_1.append(citation)
                else:
                    arr_2.append(citation)
            if len(arr_1) >= n:
                return n
            else:
                n -= 1