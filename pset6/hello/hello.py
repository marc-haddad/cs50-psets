from cs50 import get_string


# Defines 'main()' function
def main():
    # Gets name of user
    name = get_string("What is your name?\n")
    print("Hello, {}".format(name))


# Runs main()
if __name__ == "__main__":
    main()