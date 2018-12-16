"""
name:           puzzle_generator.py
language:       python 3.7
description:    generates a word search puzzle text from a given list of words
author:         awallien
"""

import sys

def usage():
    """
    :return: usage message for executing this program properly
    """
    return "Usage: python3.7 puzzle_generator.py size filename\n" \
           "    size        dimension size of resulting word search puzzle\n" \
           "    filename    the list of words"

def main():

    # error check for number of arguments passed to command line
    if len(sys.argv) != 3:
        print(usage(), file=sys.stderr)

    # error check for valid dimension size
    elif not sys.argv[1].isdigit() or sys.argv[1]=='0':
        print("Invalid dimension size (%s)" % sys.argv[1], file=sys.stderr)

    else:
        # error check for valid file
        file = None
        try:
            file = open(sys.argv[2], "r")
        except IOError:
            print("Cannot open file:", sys.argv[2], file=sys.stderr)
            exit()

        # generate word list
        wordlst = file.read().split("\n")



if __name__ == '__main__':
    main()