class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length_a = len(text1)
        length_b = len(text2)

        lcs = [[-1 for _ in range(length_b + 1)] for _ in range(length_a + 1)]
        # print(lcs)

        for i in range(length_a + 1):
            for j in range(length_b + 1):
                if i == 0 or j == 0:
                    lcs[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    lcs[i][j] = 1 + lcs[i-1][j-1]
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

        # print(lcs)
        # print(lcs[length_a][length_b])
        return lcs[length_a][length_b]

sol = Solution()
sol.longestCommonSubsequence("abcde", "ace")

# Complexity: O (length_A x length_B)
# Is better than the first approach because I don't have the full call stack anymore