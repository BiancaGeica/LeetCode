class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        nums_length = len(nums)

        best = [1 for _ in range(nums_length)]
        # print(best)

        if nums_length == 1:
            return 1

        for i in range(nums_length):
            maximum = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maximum = max(maximum, best[j])

            best[i] = 1 + maximum

        # print(best)
        # print(max(best))
        return max(best)

sol = Solution()
sol.lengthOfLIS([10, 9, 2, 5, 3, 8])

# Complexity: O(n^2)