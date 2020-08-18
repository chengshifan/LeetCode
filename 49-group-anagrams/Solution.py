from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]
        res = {}
        while len(strs) >= 1:
            s = "".join(sorted(list(strs[0])))
            if s not in res.keys():
                res[s] = [strs[0]]
            else:
                res[s].append(strs[0])
            strs.remove(strs[0])

        return [i for i in res.values()]