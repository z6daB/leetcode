# Longest Palindromic Substring with DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[False] * l for _ in range(l)]

        start = 0
        max_length = 1

        for i in range(l):
            dp[i][i] = True
        for i in range(l - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        for length in range(3, l + 1):
            for i in range(l - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_length:
                        max_length = length
                        start = i

        return s[start:start + max_length]
