# Code Solution for day6
# Time 2022-09-06

import numpy as np
import copy


class Solution:
    def __init__(self):
        self.input = open('input.txt', 'r').read().splitlines()
        self.input = list(int(x) for x in self.input[0].split(','))
        self.days = 80

    def set_days(self, days):
        self.days = days

    def solve(self, day = 0):
        fish = copy.copy(self.input)
        # O(2^n)
        while day < self.days:
            day += 1
            new_fish = []
            for i, timer in enumerate(fish):
                if timer == 0:
                    new_fish.append(8)
                    fish[i] = 6
                else:
                    fish[i] = fish[i] - 1
            fish.extend(new_fish)
        result = len(fish)
        return result

    def solve2(self, day = 0):
        number = len(self.input)
        fish = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, 'total': number}
        for i in range(1, 6):
            fish[str(i)] = self.input.count(i)
        # O(n)
        while day < self.days:
            day += 1
            fish['total'] += fish['0']
            tmp = fish['0']
            fish['0'] = fish['1']
            fish['1'] = fish['2']
            fish['2'] = fish['3']
            fish['3'] = fish['4']
            fish['4'] = fish['5']
            fish['5'] = fish['6']
            fish['6'] = fish['7'] + tmp
            fish['7'] = fish['8']
            fish['8'] = tmp

        return fish['total']


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve())
    sol.set_days(256)
    print(sol.solve2())


