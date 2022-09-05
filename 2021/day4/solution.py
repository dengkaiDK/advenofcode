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
                    numbers = list(map(int, self.input[i].split()))
                    board.append(numbers)
            # print(board) # last matrix to add
            boards.append(board)
            return boards

        self.boards = np.array(build_board())
        # print('Random numbers : {}, Random borads: {}'.format(len(self.random_order), len(self.boards)))

    def solve(self):
        mask = self.boards < 0
        result = []
        bingo = {}
        for i in self.random_order:
            for j in range(0, len(self.boards)):
                if j in bingo:
                    continue
                board = self.boards[j]
                index = np.argwhere(board == i)

                if len(index) > 0:
                    for k in range(0, len(index)):
                        mask[j][index[k][0]][index[k][1]] = True
                        if 5 in np.sum(mask[j], axis=0) or 5 in np.sum(mask[j], axis=1):
                            unmarked_sum = np.sum(board * (mask[j] == False))
                            result.append(unmarked_sum * i)
                            bingo[j] = True

        return result


if __name__ == '__main__':
    sol = Solution()
    rel = sol.solve()
    print('Part 1: {}, Part 2: {}'.format(rel[0], rel[-1]))

