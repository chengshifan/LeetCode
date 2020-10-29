from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars or len(chars) == 0:
            return 0
        if len(chars) == 1:
            return 1
        start = 0
        i = 0
        while i < len(chars):
            if chars[i] != chars[start]:
                count = i - start
                if count >= 2:
                    del chars[start + 1: i]
                    i = i - count + 1
                    for j in range(len(str(count)) - 1, -1, -1):
                        chars.insert(start + 1, list(str(count))[j])
                        i += 1
                start = i
            else:
                if i == len(chars) - 1:
                    count = i - start + 1
                    if count >= 2:
                        del chars[start + 1:]
                        for j in range(len(str(count)) - 1, -1, -1):
                            chars.insert(start + 1, list(str(count))[j])
                        break
                i += 1
        return len(chars)
