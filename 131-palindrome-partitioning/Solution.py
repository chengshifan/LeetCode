from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        temp = []

        def backTrace(res, temp):
            if not res:
                results.append(temp)
                return
            for i in range(1, len(res) + 1):
                if res[:i] == res[:i][::-1]:
                    backTrace(res[i:], temp + [res[:i]])

        backTrace(s, temp)
        return results
