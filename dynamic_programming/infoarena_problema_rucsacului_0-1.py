def knapsack_0_1(nr_objects, maximum_capacity, list_of_objects):
    object_value = [x[1] for x in list_of_objects] # list comprehension to unzip lists
    object_weight = [x[0] for x in list_of_objects]

    nr_rows_dp_matrix = nr_objects + 1 # added 1 for the "universe" with 0 objects available
    nr_columns_dp_matrix = maximum_capacity + 1 # + 1 for the knapsack with 0 capacity
    dp = [[0 for _ in range(nr_columns_dp_matrix)] for _ in range(nr_rows_dp_matrix)]

    for i in range(nr_rows_dp_matrix):
        for j in range(nr_columns_dp_matrix):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif  object_weight[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - object_weight[i - 1]] + object_value[i - 1])

    print(dp[nr_rows_dp_matrix - 1][nr_columns_dp_matrix - 1])

knapsack_0_1(4, 10, [(5, 10), (8, 19), (4, 4), (5, 10)])