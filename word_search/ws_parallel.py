"""
file: ws_sequential.py
language: python3.x
author: Alexander Wall
description: program does a parallel word search given a list of words and the board
"""

import sys

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: python3 ws_sequential.py [number of threads] [puzzle file]", file=sys.stderr)
        exit(1)

    fname = sys.argv[1]
    wordlist = []
    board = []

    with open(fname) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            board.append(line)

        wordlist = f.read().split("\n")


