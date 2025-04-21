graph = {"A": ["B", "C"], "B": ["A", "C", "D"], "C": ["A", "B", "D"], "D": ["B", "C"]}
# Available colors
colors = ["Red", "Green", "Blue"]
# To store the result
res = {}
# Greedy coloring
for node in graph:
    # Check colors of adjacent nodes
    used = [res[neighbor] for neighbor in graph[node] if neighbor in res]
    # Assign the first available color
    for color in colors:
        if color not in used:
            res[node] = color
            break
# Print result
for node in res:
    print(f"Node {node} ---> Color {res[node]}")
