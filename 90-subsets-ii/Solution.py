from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None
        res = []

        def backTrace(path, datas):
            if sorted(path) not in res:
                res.append(sorted(path)[:])
                for data in datas[:]:
                    datas.remove(data)
                    path.append(data)
                    backTrace(path, datas)
                    datas.append(data)
                    path.remove(data)
            else:
                return

        backTrace([], nums)
        return res