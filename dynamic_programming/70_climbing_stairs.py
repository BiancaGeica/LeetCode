class Solution:
    def climbStairs(self, n: int) -> int:
        arr = []
        for i in range(n + 1):
            if i <= 1:
                arr.append(1)
            else:
                arr.append(0)

        for i in range(2, n + 1):
            arr[i] = arr[i-1] + arr[i-2]

        return arr[n]

# Time complexity = theta(n)
# bottom up