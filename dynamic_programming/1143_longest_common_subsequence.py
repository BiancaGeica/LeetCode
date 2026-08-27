class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length_a = len(text1)
        length_b = len(text2)

        lcs = [[-1 for _ in range(length_b)] for _ in range(length_a)]
        # print(lcs)

        def helper(i, j):
            result = 0

            if i == -1 or j == -1:
                return 0

            if lcs[i][j] != -1:
                return lcs[i][j]
            else:
                if text1[i] == text2[j]:
                    result = 1 + helper(i-1, j-1)
                else:
                    result = max(helper(i-1, j), helper(i, j-1))

            lcs[i][j] = result
            return result

        helper(length_a - 1, length_b - 1)
        print(lcs[length_a - 1][length_b - 1])
        return lcs[length_a - 1][length_b - 1]

sol = Solution()
sol.longestCommonSubsequence("abc", "def")

# Complexity: O (length_A x length_B)
# Maximum stack length: length_A + length_B