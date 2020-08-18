from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if not strs:
            return res

        index = 0
        if strs[0]:
            common = strs[0][0]
        else:
            return res
        while True:
            for str in strs:
                if index > len(str) - 1:
                    return res if index != 0 else ''
                else:
                    if str[index] != common:
                        return res if index != 0 else ''
            index += 1
            res += common
            if index <= len(strs[0]) - 1:
                common = strs[0][index]
            else:
                return strs[0]
