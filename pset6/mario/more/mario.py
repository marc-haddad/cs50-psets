from cs50 import get_int


# Defines 'main()' function
def main():
    while(True):
        # Gets number from user
        height = get_int("Height: ")
        if height >= 1 and height <= 8:
            break
    for i in range(height + 1):
        if i == 0:
            continue
        for j in range(height - i):
            print(" ", end="")
        for k in range(height - (height - i)):
            print("#", end="")
        print("  ", end="")
        for l in range(height - (height - i)):
            print("#", end="")
        print()


# Runs main()
if __name__ == "__main__":
    main()