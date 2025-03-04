class Solution:
    def minDistance(self, word1: str, word2: str):
        length1 = len(word1)
        length2 = len(word2)

        dp = [[float('inf')] * (length2 + 1) for _ in range(length1 + 1)]

        for j in range(length2 + 1):
            dp[length1][j] = length2 - j
        for i in range(length1 + 1):
            dp[i][length2] = length1 - i

        for i in range(length1 - 1, -1, -1):
            for j in range(length2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]
