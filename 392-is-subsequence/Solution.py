class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        for i in range(0, len(t)):
            if t[i] == s[0]:
                return self.isSubsequence(s[1:], t[i+1:])
        return False


print(Solution().isSubsequence(s="aaaaaa", t="bbaaa"))
