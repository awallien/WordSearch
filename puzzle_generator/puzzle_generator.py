"""
name:           puzzle_generator.py
language:       python 3.7
description:    generates a word search puzzle text from a given list of words
author:         awallien
"""
import random
import sys

EMPTY_FILL = " "

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

        def empty_board():
            """
            Create an empty, blank puzzle board
            :return: the board
            """
            return [[EMPTY_FILL for i in range(self.max_len)] for j in range(self.max_len)]

        def fill_board(wordlist, stack):
            """
            private function to DFS backtrack until we get a valid board with all words on it
            :return: the final config board if all words can fit on the board, None otherwise
            """

            if not wordlist:
                return stack[-1]

            # for each word
            #   get a layout: vertical, horizontal, or diagonal
            #   get an x and y coordinate
            for word in wordlist:
                for layout in random.sample(range(len(self.layword)), len(self.layword)):
                    for i in random.sample(range(self.max_len), self.max_len):
                        for j in random.sample(range(self.max_len), self.max_len):
                            new_config = self.layword[layout](word, stack[-1], i, j)
                            if new_config:
                                stack.append(new_config)
                                if fill_board(wordlist[1:], stack):
                                    return stack[-1]

            return None

        # get dimension size of longest word and make board
        self.max_len = len(max(self.wordlist, key=len))*2

        stack = list()
        stack.append(empty_board())
        self.board = fill_board(self.wordlist, stack)

        # a board cannot be made for this word of list
        if not self.board:
            print("Unable to make board with given list", file=sys.stderr)
            exit(1)

        self.__random_filler()

    def __vertical(self, word, board, x, y):
        """
        Place the word vertically on the board
        :param word: the word to put on board
        :param board: the instance of board
        :param x: the x coordinate
        :param y: the y coordinate
        :return: the new board if the word can fit; otherwise, None
        """
        # print("vertical")

        length = len(word)
        if y + length > self.max_len:
            return None

        # check the slots on the board starting at board[x,y]
        # is there a letter already occupying a spot
        for k in range(length):
            if board[x][y + k] != EMPTY_FILL and board[x][y + k] != word[k]:
                return None

        # should the word be reversed?
        if random.randint(0, 1):
            word = word[::-1]

        # lay the word down
        for k in range(length):
            board[x][y + k] = word[k]

        return board

    def __horizontal(self, word, board, x, y):
        """
        Put the word horizontally on the board
        :param word: the word to put on board
        :param board: the instance of board
        :param x: the x coordinate
        :param y: the y coordinate
        :return: the new board if word can fit; otherwise, None
        """
        # print("horizontal")

        length = len(word)
        if x + length > self.max_len:
            return None

        for k in range(length):
            if board[x + k][y] != EMPTY_FILL and board[x + k][y] != word[k]:
                return None

        if random.randint(0, 1):
            word = word[::-1]

        for k in range(length):
            board[x + k][y] = word[k]

        return board

    def __diagonal(self, word, board, x, y):
        """
        Put the word diagonally on the board
        :param word: the word
        :param board: the instance of board
        :param x: the x coordinate to insert word
        :param y: the y coordinate to insert word
        :return: the new board if the words fits; otherwise, None
        """
        # print("diagonal")

        length = len(word)
        if x + length > self.max_len or y + length > self.max_len:
            return None

        for k in range(length):
            if board[x + k][y + k] != EMPTY_FILL and board[x + k][y + k] != word[k]:
                return None

        word = word[::-1] if random.randint(0, 1) else word

        for k in range(length):
            board[x + k][y + k] = word[k]

        return board

    def __random_filler(self):
        """
        Fill the empty spots on the puzzle board with random letters
        :return: None
        """
        for row in range(self.max_len):
            for col in range(self.max_len):
                if self.board[row][col] == EMPTY_FILL:
                    self.board[row][col] = chr(random.randrange(ord('a'), ord('z')))

    def output(self,fname=""):
        """
        Writes the puzzle and list of words to a text file
        :return: None
        """

        # will use later, right now, testing purposes
        # hashcode = hash(self)%(10**6)
        # out = open("puzzle"+str(hashcode), "w")
        out = ""
        if not fname:
            hashcode = hash(self)%(10**6)
            if hashcode < 0:
                hashcode *= -1
            out = open("puzzle"+str(hashcode), "w")
        else:
            out = open(fname, "w")

        for row in range(self.max_len):
            for col in range(self.max_len):
                if col == self.max_len - 1:
                    out.write(self.board[row][col] + "\n")
                else:
                    out.write(self.board[row][col] + " ")

        out.write("\n")

        for idx in range(len(self.wordlist)):
            if idx == len(self.wordlist) - 1:
                out.write(self.wordlist[idx])
            else:
                out.write(self.wordlist[idx] + "\n")



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
                WordSearchPuzzle(wordlist).output("test")

        except IOError:
            print("Cannot open file:", sys.argv[1], file=sys.stderr)
            exit()
