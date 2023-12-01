for i in range(6, 0, -1):
    for j in range(1, i + 1):
        if i == 6 or j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
