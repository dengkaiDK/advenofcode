# Code Solution for day 13
# Time 2022-09-14
import numpy as np
import copy


class Solution:
    def __init__(self):
        self.input = open('input.txt', 'r').read().splitlines()
        self.dots = np.zeros((1311, 895), dtype=np.int8)
        self.fold = []
        for i, row in enumerate(self.input):
            if i < 907:
                x, y = row.split(',')
                self.dots[int(x), int(y)] = 1
            elif i > 907:
                _, _, line = row.split()
                axis, number = line.split('=')
                self.fold.append((axis, int(number)))

    def run(self):
        order = self.fold[0]
        w, h = self.dots.shape
        dots_after_fold = 0
        if order[0] == 'x':
            self.newdots = np.zeros((w // 2, h), dtype=np.int8)
            for i in range(w // 2):
                for j in range(h):
                    self.newdots[i, j] = min(1, self.dots[i, j] + self.dots[w - i -1, j])
            dots_after_fold = np.sum(self.newdots)
        elif order[0] == 'y':
            self.newdots = np.zeros((w, h // 2), dtype=np.int8)
            for i in range(h // 2):
                for j in range(w):
                    self.newdots[j, i] = min(1, self.dots[j, i] + self.dots[j, h - i - 1])
            dots_after_fold = np.sum(self.newdots)
        return dots_after_fold

    def run2(self):
        w, h = self.dots.shape
        dots = copy.copy(self.dots)
        while len(self.fold) > 0:
            order = self.fold.pop(0)
            if order[0] == 'x':
                newdots = np.zeros((w // 2, h), dtype=np.int8)
                for i in range(w // 2):
                    for j in range(h):
                        newdots[i, j] = min(1, dots[i, j] + dots[w - i -1, j])
                dots = newdots
            elif order[0] == 'y':
                newdots = np.zeros((w, h // 2), dtype=np.int8)
                for i in range(h // 2):
                    for j in range(w):
                        newdots[j, i] = min(1, dots[j, i] + dots[j, h - i - 1])
                dots = newdots
            w, h = dots.shape

        return dots


if __name__ == '__main__':
    solution = Solution()
    print(solution.run())
    dots = solution.run2()
    # print(dots.shape)
    for i in range(8):
        print(dots[5*i:5*(i+1),:])
        print()
    # hint: look vertically and flip along y = 0 axis