def knapsack_0_1(nr_objects, maximum_capacity, list_of_objects):
    object_value = [x[1] for x in list_of_objects] # list comprehension to unzip lists
    object_weight = [x[0] for x in list_of_objects]

    nr_columns_dp_matrix = maximum_capacity + 1 # + 1 for the knapsack with 0 capacity
    dp = [[0 for _ in range(nr_columns_dp_matrix)] for _ in range(2)]

    for i in range(1, nr_objects + 1):
        current_row = i % 2
        previous_row = 1 - current_row

        for j in range(nr_columns_dp_matrix):
            if j == 0:
                dp[current_row][j] = 0
            elif  object_weight[i - 1] > j:
                dp[current_row][j] = dp[previous_row][j]
            else:
                dp[current_row][j] = max(dp[previous_row][j], dp[previous_row][j - object_weight[i - 1]] + object_value[i - 1])

    return dp[nr_objects % 2][nr_columns_dp_matrix - 1]

# knapsack_0_1(4, 10, [(5, 10), (8, 19), (4, 4), (5, 10)])

file = open("rucsac.in", "r")
first_line = file.readline()
list_for_the_first_line = first_line.split()

nr_of_objects = int(list_for_the_first_line[0])
# print(nr_of_objects)
capacity_backpack = int(list_for_the_first_line[1])
# print(capacity_backpack)

objects = []
for line in file:
    line = line.strip()
    if not line:
        continue
    weight, value = line.split()
    objects.append((int(weight), int(value)))

with open("rucsac.out", "w") as file:
    file.write(str(knapsack_0_1(nr_of_objects, capacity_backpack, objects)))

# Time complexity: O(knapsack_capacity)