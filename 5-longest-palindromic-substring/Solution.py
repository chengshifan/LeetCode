class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0 or len(s) == 1:
            return s
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        begin, end = 0, 0
        max_value = 1
        for i in range(0, n):
            if n - i < max_value:
                break
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                else:
                    if i == 0:
                        if s[0:j + 1] == s[j::-1]:
                            dp[i][j] = len(s[0:j + 1])
                        else:
                            dp[i][j] = dp[i][j - 1]
                    else:
                        if s[i:j + 1] == s[j:i - 1:-1]:
                            dp[i][j] = len(s[i:j + 1])
                        else:
                            dp[i][j] = dp[i][j - 1]
                    if dp[i][j] > max_value:
                        begin = i
                        end = j
                        max_value = dp[i][j]

        return s[begin:end + 1]
