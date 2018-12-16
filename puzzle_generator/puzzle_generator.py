"""
name:           puzzle_generator.py
language:       python 3.7
description:    generates a word search puzzle text from a given list of words
author:         awallien
"""
import random, sys

class WordSearchPuzzle:
    """
    The class that constructs the puzzle board and word list
    """
    def __init__(self, wordlist):
        """
        Constructor
        :param wordlist: list of words to insert into the puzzle
        """
        self.layword = [self.__horizontal, self.__vertical, self.__diagonal]
        self.wordlist = wordlist
        self.max_len = 0
        self.board = None

        self.__make_board()

    def __make_board(self):
        """
        makes the word search puzzle board
        :return:
        """
        def fill_board(wordlist, stack):
            """
            private function to DFS backtrack until we get a valid board with all words on it
            :return:
            """
            pass


        # get dimension size of longest word and make board
        self.max_len = len(max(self.wordlist, key=len))*2
        self.board = [[""]*self.max_len]*self.max_len
        fill_board(self.wordlist, list(self.board))

    def __horizontal(self, word):
        print("horizontal")

    def __vertical(self, word):
        print("vertical")

    def __diagonal(self, word):
        print("diagonal")

    def output(self):
        """
        Writes the puzzle and list of words to a text file
        :return: None
        """

        # will use later, right now, testing purposes
        #hashcode = hash(self)%(10**6)
        #out = open("puzzle"+str(hashcode), "w")

        out = open("test", "w")

        for row in range(self.max_len):
            for col in range(self.max_len):
                if col == self.max_len-1:
                    out.write(self.board[row][col]+"\n")
                else:
                    out.write(self.board[row][col]+" ")

        out.write("\n")

        for idx in range(len(self.wordlist)):
            if idx == len(self.wordlist)-1:
                out.write(self.wordlist[idx])
            else:
                out.write(self.wordlist[idx]+"\n")

if __name__ == '__main__':
    """
    As a standalone program, used to make a text file that contains the puzzle board
    and the list of words
    :return: None
    """

    # error check for number of arguments passed to command line
    if len(sys.argv) != 2:
        print("Usage: python3.7 puzzle_generator.py word_list", file=sys.stderr)

    else:
        # error check for valid file
        file = None
        try:
            file = open(sys.argv[1], "r")
            wordlist = file.read().split("\n")

            # check for empty file
            if not wordlist[0]:
                print("Reading empty file", file=sys.stderr)

            else:
                WordSearchPuzzle(wordlist).output()


        except IOError:
            print("Cannot open file:", sys.argv[1], file=sys.stderr)
            exit()
