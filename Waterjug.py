j1, j2 = 0, 0  # current water in jug1 and jug2
x, y = 4, 3    # capacities of jug1 and jug2

print("Initial state = (0, 0)")
print("Goal state = (2, 0)")

while True:
    print(f"Current state = ({j1}, {j2})")
    if j1 == 2 and j2 == 0:
        print("Goal reached!")
        break

    print("Rules:")
    print("1. Fill 4L jug\n2. Fill 3L jug\n3. Empty 4L jug\n4. Empty 3L jug")
    print("5. Pour 4L → 3L\n6. Pour 3L → 4L\n7. Pour all 4L → 3L\n8. Pour all 3L → 4L")

    r = int(input("Enter rule number (1-8): "))

    if r == 1:
        j1 = x
    elif r == 2:
        j2 = y
    elif r == 3:
        j1 = 0
    elif r == 4:
        j2 = 0
    elif r == 5:
        t = min(j1, y - j2)
        j1 -= t
        j2 += t
    elif r == 6:
        t = min(j2, x - j1)
        j2 -= t
        j1 += t
    elif r == 7:
        j2 += j1
        j1 = 0
        if j2 > y:
            j2 = y
    elif r == 8:
        j1 += j2
        j2 = 0
        if j1 > x:
            j1 = x
    else:
        print("Invalid rule.")
