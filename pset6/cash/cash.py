# Marc Omar Haddad
# CS50 - pset6: 'Cash'
# September 3, 2019

from cs50 import get_float

# This program returns the least amount of coins to be returned in change


def main():

    # Initializes vars
    c, coins = 0, 0

    # Checks to make sure user inputs positive float
    while c <= 0:
        c = get_float("Change owed: ")

    c = round(c * 100)

    # Creates custom list of types of change
    list = [25, 10, 5]

    # Iterates through the list in order
    for i in range(len(list)):
        coins += (c - (c % list[i])) / list[i]
        c = c % list[i]

    coins += c

    print(int(coins))


if __name__ == "__main__":
    main()
