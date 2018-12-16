"""
name:           puzzle_generator.py
language:       python 3.7
description:    generates a word search puzzle text from a given list of words
author:         awallien
"""
import sys


def main():

    # error check for number of arguments passed to command line
    if len(sys.argv) != 2:
        print("Usage: python3.7 puzzle_generator.py word_list", file=sys.stderr)

    else:
        # error check for valid file
        file = None
        try:
            file = open(sys.argv[1], "r")
        except IOError:
            print("Cannot open file:", sys.argv[1], file=sys.stderr)
            exit()


if __name__ == '__main__':
    main()