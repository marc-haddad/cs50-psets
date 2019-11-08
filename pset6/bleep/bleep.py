# Marc Omar Haddad
# CS50 - pset6: "Bleep"
# September 6, 2019


from cs50 import get_string
from sys import argv
import re

# This program asks for an input from the user and outputs a censored version


def main():

    # Checks for correct number of args
    if (len(argv) != 2):
        print("Usage: python bleep.py dictionary")
        exit(1)

    # Opens file containing words to be censored
    dic_file = open(argv[1], 'r')

    # Reads file and places each line (i.e. single words) into a string within a list
    dic_list = dic_file.readlines()

    # Strips any trailing new lines
    strip_dic = [word.strip() for word in dic_list]

    dic_file.close()

    # Prompts user for string to be censored
    inpu = get_string("What message would you like to censor? ")

    # Converts text to lower-case for comparison
    inpu_low = inpu.lower()

    pattern = re.compile('\W')

    # Replaces any non-alphanumeric chars with a space
    inpu_low = re.sub(pattern, ' ', inpu_low)

    # Creates list from string with each member being individual word
    inpu_low_list = inpu_low.split(' ')

    # Replaces any non-alphanumeric chars with a space, but maintains original letter-case
    inpu = re.sub(pattern, ' ', inpu)

    # Creates case-sensitive list from string with each member being individual word
    inpu_list = inpu.split(' ')

    # Iterates over inputed list (lower-case) and compares each word to list of 'bad' words
    for i in range(len(inpu_list)):

        for j in range(len(strip_dic)):

            # If a bad word is found, replaces bad word in case-sensitive list with '*'
            if (strip_dic[j] == inpu_low_list[i]):

                inpu_list[i] = '*' * len(inpu_list[i])

    # Converts case-sensitive list to string and prints
    outpu_str = ' '.join(inpu_list)

    print(outpu_str)

    return 0


if __name__ == "__main__":
    main()
