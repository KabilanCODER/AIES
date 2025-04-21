goal = ["a", "b", "c", "d", "e"]
result = []


def solve(table, step=0):
    if step == len(goal):  # All blocks placed correctly
        return True

    print(f"\nTrying to place goal[{step}] = '{goal[step]}'")
    for i in range(len(table)):
        block = table[i]
        print(f"  Checking table[{i}] = '{block}'", end=" → ")

        if block == goal[step]:
            print("✅ Match found. Placing it.")
            block = table.pop(i)
            result.append(block)
            print("  Current Result:", result)

            if solve(table, step + 1):
                return True

        else:
            print("❌ Not a match.")

    print(f"⚠️ No match for goal[{step}] = '{goal[step]}' at this level.")
    return False


# Main program
problem = ["c", "a", "e", "d", "b"]
print("Start Table:", problem)
print("Goal Order:", goal)

if solve(problem.copy()):
    print("\n🎉 Goal Achieved! Final Result:", result)
else:
    print("\n❌ Goal Not Achievable.")
