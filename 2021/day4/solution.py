# Code Solution for day4
# Time 2022-09-04
import numpy as np


class Solution:
    def __init__(self):
        self.input = open('input.txt', 'r').read().splitlines()
        self.random_order = list(map(int, self.input[0].split(',')))

        def build_board():
            lines = len(self.input)
            boards = []
            board = []
            for i in range(2, lines):
                if self.input[i] == '':
                    boards.append(board)
                    board = []
                else:
                    numbers = list(map(int,self.input[i].split()))
                    board.append(numbers)
            # print(board) # last matrix to add
            boards.append(board)
            return boards

        self.boards = np.array(build_board())
        print('Random numbers : {}, Random borads: {}'.format(len(self.random_order), len(self.boards)))

    def solve(self):
        pass



if __name__ == '__main__':
    sol = Solution()