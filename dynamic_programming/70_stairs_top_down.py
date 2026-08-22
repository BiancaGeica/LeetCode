class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [-1 for i in range(n + 1)]

        def helper_climbStairs(nr):
            if nr <= 1:
                return 1

            if arr[nr] != -1:
                return arr[nr]
            else:
                arr[nr] = helper_climbStairs(nr - 1) + helper_climbStairs(nr - 2)

            return arr[nr]

        print(helper_climbStairs(n))
        return helper_climbStairs(n)

#sol = Solution()
#sol.climbStairs(5)
# Time complexity = theta(n)
# top down