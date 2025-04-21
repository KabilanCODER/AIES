from collections import deque

# Goal state
goal_state = "123456780"  # '0' is the empty space
# Moves based on the index of '0' in the string
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7],
}


# Swap characters in string
def swap(state, i, j):
    state = list(state)
    state[i], state[j] = state[j], state[i]
    return "".join(state)


# Helper to print board nicely
def print_board(state):
    print()
    for i in range(0, 9, 3):
        print(" ".join(state[i : i + 3]))


# BFS function
def bfs(start_state):
    queue = deque()
    visited = set()
    queue.append((start_state, []))  # (state, path)
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            print("Solved! Path to goal:")
            for step in path + [current_state]:
                print_board(step)
            return
        visited.add(current_state)
        zero_pos = current_state.index("0")  # find blank space
        for move in moves[zero_pos]:
            new_state = swap(current_state, zero_pos, move)
            if new_state not in visited:
                queue.append((new_state, path + [current_state]))


# Example usage
start = "724506831"
start2 = "123450678"
print("Initial State:")
print_board(start2)
print("Goal State:")
print_board(goal_state)
bfs(start2)
