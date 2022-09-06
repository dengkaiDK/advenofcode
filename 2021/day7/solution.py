# Code Solution for day7
# Time 2022-09-06

import math
import numpy as np


class Solution:
    def __init__(self):
        self.input = list(int(x) for x in open("input.txt").read().split(","))
        self.input = np.array(self.input)
        # print(self.input.shape)

    def run(self):
        mid =  np.median(self.input)
        return np.sum(np.abs(np.subtract(self.input, mid)))

    def run2(self):
        mid = int(np.median(self.input))
        mean = int(np.mean(self.input))
        cost = math.inf
        fuel = lambda x: (1 + x) * x/2
        for i in range(mid, mean + 1):
            temp = np.sum(list(map(fuel, np.abs(self.input - i))))
            if cost > temp:
                cost = temp
        return cost


if __name__ == "__main__":
    sol = Solution()
    print(sol.run())
    print(sol.run2())