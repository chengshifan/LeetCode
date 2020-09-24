from collections import Counter
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s or len(s) < 11:
            return []
        begin, end = 0, 10
        ans = []
        datas = []
        while begin < len(s) and end <= len(s):
            target = s[begin:end]
            datas.append(target)
            begin += 1
            end += 1
        for k, v in Counter(datas).items():
            if v > 1 and k not in ans:
                ans.append(k)
        return ans
