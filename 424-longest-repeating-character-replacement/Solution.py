class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "" or not s:
            return 0
        left, right = 0, 0
        records = {}
        n = len(s)
        max_record = 0
        max_len = 0
        while right in range(n):
            ch = s[right]
            if ch not in records.keys():
                records[ch] = 1
            else:
                records[ch] += 1
            max_record = max(max_record, records[ch])
            if right - left + 1 - max_record > k:
                records[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
