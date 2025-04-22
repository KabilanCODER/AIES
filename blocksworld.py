# Initial state
initial = ["c", "a", "e", "d", "b"]

# Goal state
goal = ["a", "b", "c", "d", "e"]

# Result list
result = []

# Simple planner to create goal from initial
for block in goal:
    if block in initial:
        result.append(block)
    else:
        print(f"Block {block} not found in initial state!")

# Output
print("Initial:", initial)
print("Goal:", goal)
print("Planned Result:", result)

# Check success
if result == goal:
    print("Goal achieved successfully!")
else:
    print("Goal not achieved.")
