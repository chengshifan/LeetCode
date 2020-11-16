from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        if min(citations) > n:
            return n
        while n >= 0:
            count = 0
            for citation in citations:
                if citation >= n:
                    count += 1
                if count >= n:
                    return n

            if count >= n:
                return n
            else:
                n -= 1
