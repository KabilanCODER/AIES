import random
def obj(x):
    return -(x - 3) ** 2 + 9 

def hill_climb(start, step_size=0.1, max_iterations=100):
    current = start  
    for _ in range(max_iterations):
        neighbors = [current + step_size, current - step_size]  
        next_move = max(neighbors, key=obj)  

        if obj(next_move) <= obj(current):
            break 
        current = next_move  
    return current, obj(current)

start_point = random.uniform(-10, 10)  
solution, value = hill_climb(start_point)
print("Optimal Solution:", solution)
print("Objective Function Value:", value)
