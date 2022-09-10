# Code Solution for day 9
# Time 2022-09-10

import numpy as np


class Solution:
    def __init__(self):
        self.input = open('input.txt', 'r').read().splitlines()
        self.input = np.array([list(row) for row in self.input], dtype=np.int64)
        # print(self.input.shape)

    def run1(self):
        risk_level_sum = 0
        low_point = []
        w, h = self.input.shape
        for i in range(w):
            for j in range(h):
                up = self.input[i - 1, j] if i > 0 else 10
                left = self.input[i, j - 1] if j > 0 else 10
                down = self.input[i + 1, j] if i < w - 1 else 10
                right = self.input[i, j + 1] if j < h - 1 else 10
                lowest = min(up, left, down, right)
                if self.input[i, j] < lowest:
                    risk_level_sum += self.input[i, j] + 1
                    low_point.append((i, j))

        return risk_level_sum, low_point

    def run2(self):
        basins = []
        low_point = self.run1()[1]
        look_up = {}
        w, h = self.input.shape

        def find_basin_size(i, j):
            if (i, j) in look_up:
                return 0
            if self.input[i, j] == 9:
                return 0
            else:
                look_up[(i, j)] = 1
                up = find_basin_size(i - 1, j) if i > 0 else 0
                left = find_basin_size(i, j - 1) if j > 0 else 0
                down = find_basin_size(i + 1, j) if i < w - 1 else 0
                right = find_basin_size(i, j + 1) if j < h - 1 else 0
                return sum([up, left, down, right]) + look_up[(i, j)]

        for point in low_point:
            basins.append(find_basin_size(point[0], point[1]))
            number = len(basins)
            while number > 1:
                if basins[number - 1] < basins[number - 2]:
                    basins[number - 2], basins[number - 1] = basins[number - 1], basins[number - 2]
                number -= 1

        return basins[-1] * basins[-2] * basins[-3]


if __name__ == '__main__':
    sol = Solution()
    print(sol.run1()[0])
    print(sol.run2())