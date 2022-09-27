# Code Solution for day 17
# Time: 2022-09-26
import numpy as np
# import time


class Solution:
    def __init__(self, target):
        self.x_range = target[0], target[1]
        self.y_range = target[2], target[3]

    def height(self, y:int) -> int:
        assert y >= 0
        return (y + 1) * y // 2

    def forward(self, x:int) -> int:
        return (x + 1) * x // 2

    def check_trajectory(self, x:int, y:int):
        move = [(0, 0)]
        assert x >= 0
        # if x is too small, cannot reach target area.
        if self.forward(x) < self.x_range[0]:
            return move, False

        flag = False
        while True:
            position = move[-1]
            if position[0] + x > self.x_range[1]:
                break
            if position[1] + y < self.y_range[1]:
                break

            move.append((position[0] + x, position[1] + y))
            if position[1] + y <= self.y_range[0] and position[0] + x >= self.x_range[0]:
                flag = True

            x -= 1 if x > 0 else 0
            y -= 1
        return move, flag

    def part1(self):
        # the highest distance is when velocity in y axis equals to max(position[y]) - 1
        return self.height(-self.y_range[1] - 1)

    def part2(self):
        vx = np.arange(0, self.x_range[1]+1, step=1)
        vy = np.arange(-self.y_range[1] - 1, self.y_range[1] - 1, step=-1)
        unique = 0
        candidates = []
        for i in vx:
            for j in vy:
                _, flag = self.check_trajectory(i, j)
                if flag:
                    unique += 1
                    candidates.append((i, j))

        return unique, candidates


if __name__ == "__main__":
    target = list(map(int, input().split())) # input example: 29 73 -194 -248
    solution = Solution(target)
    print(solution.part1())
    # start = time.time()
    number, velocity = solution.part2()
    # end = time.time()
    print(number)
    # print('Running time: %s Seconds' % (end - start))
