from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        datas = sorted(dict(Counter(s)).items(), key=lambda x: x[1], reverse=True)
        ans = ''
        for data in datas:
            ans += data[0] * data[1]
        return ans
