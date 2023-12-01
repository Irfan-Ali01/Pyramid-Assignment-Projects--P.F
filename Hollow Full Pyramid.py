for i in range(1, 7 + 1):
    print(" " * (7 - i), end="")
    if i == 1 or i == 7:
        print("* " * i)
    else:
        print("*" + " " * (2 * i - 3) + "*")
