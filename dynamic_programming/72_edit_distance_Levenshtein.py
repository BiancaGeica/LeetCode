class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length_word1 = len(word1)
        length_word2 = len(word2)

        dp = [[0 for _ in range(length_word2 + 1)] for _ in range(length_word1 + 1)]
        # +1 for the case with both strings empty
        # print(dp)

        for i in range(length_word1 + 1):
            for j in range(length_word2 + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j -1])

        # print(dp)
        # print(dp[length_word1][length_word2])
        return dp[length_word1][length_word2]

sol = Solution()
sol.minDistance("horse", "ros")

# Complexity: O(n x m)