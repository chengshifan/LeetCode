from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = -float('inf')
        cnt = 0
        for i in intervals:
            start = i[0]
            if start >= end:
                cnt += 1
                end = i[1]
        return (len(intervals) - cnt)