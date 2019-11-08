# Marc Omar Haddad
# CS50 - pset6: 'Credit'
# September 4, 2019

from cs50 import get_string

# This program uses Luhn's algorithm to check the validity and type of credit cards


def main():

    num = get_string("Number: ")

    # Repeatedly prompts user for valid numeric input
    while (num.isdigit() != True):
        num = get_string("Number: ")

    # Checks if string is the correct length and if the first 2 chars are valid
    if (
        (len(num) != 13 and len(num) != 15 and len(num) != 16)
        or (num[0] + num[1] != ("34")
            and num[0] + num[1] != ("37")
            and num[0] + num[1] != ("51")
            and num[0] + num[1] != ("52")
            and num[0] + num[1] != ("53")
            and num[0] + num[1] != ("54")
            and num[0] + num[1] != ("55")
            and num[0] != ("4"))
    ):
        print('INVALID')

    # Checks the result of custom boolean function luhn()
    if luhn(num) == False:
        print('INVALID')
        return 1

    # Passing all previous checks means the provided num is valid

    # Checks the 'type' of credit card
    else:
        if (num[0] == '3'):
            print('AMEX')

        elif (num[0] == '4'):
            print('VISA')

        else:
            print('MASTERCARD')
        return 0


# Boolean function that takes a numeric string as input and applies Luhn's algorithm for validity
def luhn(stri):

    # Initializes the variable that will contain total sum
    add = 0

    # Iterates over the string moving backwards starting from the before-last digit, skipping every other digit
    for i in range(-2, -(len(stri) + 1), -2):

        # Converts from char to int and multiplies by 2
        x = int(stri[i]) * 2

        # If result has 2 digits, add one individual digit to the other
        if x > 9:
            x = x % 10 + ((x - (x % 10)) / 10)
            add += x

        # If result has 1 digit, add it directly
        else:
            add += x

    # Iterates over the rest of the string backwards
    for i in range(-1, -(len(stri) + 1), -2):

        # Converts chars to ints
        x = int(stri[i])

        # Adds digits as-is to total sum
        add += x

    # Checks to see if total sum is divisible by 10 (thus satisfying the conditions of Luhn's algorithm)
    if (add % 10 == 0):
        return True

    else:
        return False


if __name__ == "__main__":
    main()
