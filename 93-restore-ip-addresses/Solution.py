from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if not s:
            return res
        n = len(s)
        if n > 12 or n < 4:
            return res
        else:
            for i in range(1, n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        if i != j and i != k and j != k and 0 <= int(s[0:i]) <= 255 and 0 <= int(s[i:j]) <= 255 and 0 <= int(s[j:k]) <= 255 and 0 <= int(s[k:]) <= 255:
                            if (len(s[0:i]) > 1 and int(s[0]) == 0) or (len(s[i:j]) > 1 and int(s[i]) == 0) or (len(s[j:k]) > 1 and int(s[j]) == 0) or (len(s[k:]) > 1 and int(s[k]) == 0):
                                continue
                            else:
                                res.append(s[0:i] + '.' + s[i:j] + '.' + s[j:k] + '.' + s[k:])
        return res