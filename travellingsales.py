import itertools

# Distance matrix between 4 cities (0, 1, 2, 3)
# For example, distance from city 0 to city 1 is 10
distance_matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
num_cities = len(distance_matrix)
cities = list(range(num_cities))
# Store the shortest path and cost
min_path = None
min_cost = float("inf")
# Try all permutations of cities (except starting city fixed at 0)

for perm in itertools.permutations(cities[1:]):  # start from city 0
    current_path = [0] + list(perm) + [0]  # path must return to start
    cost = 0
    for i in range(len(current_path) - 1):
        cost += distance_matrix[current_path[i]][current_path[i + 1]]
    if cost < min_cost:
        min_cost = cost
        min_path = current_path

# Print result
print("Shortest path:", min_path)
print("Minimum cost:", min_cost)
