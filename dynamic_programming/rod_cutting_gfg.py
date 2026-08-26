class Solution:
    def cutRod(self, price: list[int]) -> int:
        rod_total_length = len(price)
        arr = [-1 for _ in range(rod_total_length)]

        def helper(i):
            if i == 0:
                return 0

            aux = price[i - 1]
            if arr[i - 1] != -1:
                return arr[i - 1]
            else:
                for j in range(1, int(i/2 + 1)):
                    aux = max(aux, helper(j) + helper(i - j))

            arr[i - 1] = aux

            return aux

        result = helper(rod_total_length)
        print(result)
        return result

sol = Solution()
sol.cutRod([3])

# personal idea
# Complexity: O(n^2)