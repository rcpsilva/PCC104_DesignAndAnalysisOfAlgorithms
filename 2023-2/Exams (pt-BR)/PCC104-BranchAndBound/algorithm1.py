for i in range(0, r):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(r, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")