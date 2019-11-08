# Marc Omar Haddad
# CS50 - pset6: Crack
# September 6, 2019

from sys import argv
import crypt
from string import ascii_letters

# This program decrypts hashed passwords up to 5 chars long through brute force


def main():

    if len(argv) != 2:
        print("Usage: python crack.py hash")
        return 1

    # Identifies salt
    salt = argv[1][0] + argv[1][1]

    word = "a"

    cry = crypt.crypt(word, salt)

    # Iterates over lowercase and uppercase alphabet over 1 char
    for a in ascii_letters:
        word = a
        cry = crypt.crypt(word, salt)
        if (cry == argv[1]):
            print(word)
            return 0

    # Iterates over lowercase and uppercase alphabet over 2 chars
    for a in ascii_letters:
        for b in ascii_letters:
            word = a + b
            cry = crypt.crypt(word, salt)
            if (cry == argv[1]):
                print(word)
                return 0

    # Iterates over lowercase and uppercase alphabet over 3 chars
    for a in ascii_letters:
        for b in ascii_letters:
            for c in ascii_letters:
                word = a + b + c
                cry = crypt.crypt(word, salt)
                if (cry == argv[1]):
                    print(word)
                    return 0

    # Iterates over lowercase and uppercase alphabet over 4 chars
    for a in ascii_letters:
        for b in ascii_letters:
            for c in ascii_letters:
                for d in ascii_letters:
                    word = a + b + c + d
                    cry = crypt.crypt(word, salt)
                    if (cry == argv[1]):
                        print(word)
                        return 0

    # Iterates over lowercase and uppercase alphabet over 5 chars
    for a in ascii_letters:
        for b in ascii_letters:
            for c in ascii_letters:
                for d in ascii_letters:
                    for e in ascii_letters:
                        word = a + b + c + d + e
                        cry = crypt.crypt(word, salt)
                        if (cry == argv[1]):
                            print(word)
                            return 0
    print("Could not decrypt")
    return 1


if __name__ == "__main__":
    main()