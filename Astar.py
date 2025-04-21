# Heuristic values (h(n)) - how far each node is from the goal G
h = {"A": 11, "B": 6, "C": 99, "D": 1, "E": 7, "G": 0}

# Graph with distances (g(n)) from one node to another
graph = {
    "A": [("B", 2), ("E", 3)],
    "B": [("C", 1), ("G", 9)],
    "C": [],
    "D": [("G", 1)],
    "E": [("D", 6)],
    "G": [],
}


def a_star(start, goal):
    open_list = [start]  # Stores nodes to be checked
    path = {}  # To store the parent of each node
    g_cost = {start: 0}  # Distance from start to current node

    while open_list:
        # Pick the node with lowest f(n) = g(n) + h(n)
        current = min(open_list, key=lambda x: g_cost.get(x, float("inf")) + h[x])

        # If we reached the goal
        if current == goal:
            result = [current]
            while current in path:
                current = path[current]
                result.append(current)
            result.reverse()
            print("Shortest Path:", result)
            return

        open_list.remove(current)

        for neighbor, cost in graph[current]:
            total_cost = g_cost[current] + cost

            if neighbor not in g_cost or total_cost < g_cost[neighbor]:
                g_cost[neighbor] = total_cost
                path[neighbor] = current
                if neighbor not in open_list:
                    open_list.append(neighbor)

    print("No path found!")


# Run the code
a_star("A", "G")
