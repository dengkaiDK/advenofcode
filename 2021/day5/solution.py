# Code Solution for day5
# Time 2022-09-05

import numpy as np

class Solution:
    def __init__(self):
        self.input = open('input.txt', 'r').read().splitlines()

        def build_coordinates():
            result = []
            for row in self.input:
                a, b = row.split('->')
                x1, y1 = a.split(',')
                x2, y2 = b.split(',')
                result.append([int(x1), int(y1), int(x2), int(y2)])
            return result
        self.coordinates = np.array(build_coordinates())
        print(self.coordinates.shape)

    def reset(self):
        x1, y1, x2, y2 = np.max(self.coordinates, axis=0)
        maxx = max(x1, x2)
        maxy = max(y1, y2)
        points = np.zeros((maxx + 1, maxy + 1), dtype=int)
        return points

    def solve(self):
        points = self.reset()
        for i in range(0, len(self.coordinates)):
            x1, y1, x2, y2 = self.coordinates[i]
            if x1 == x2 or y1 == y2:
                points[x1:x2 + 1, y1:y2 + 1] += 1
                points[x2:x1 + 1, y2:y1 + 1] += 1

        result = np.sum(points >= 2)
        return result

    def solve2(self):
        points = self.reset()
        for i in range(0, len(self.coordinates)):
            x1, y1, x2, y2 = self.coordinates[i]
            if x1 == x2 or y1 == y2:
                points[x1:x2 + 1, y1:y2 + 1] += 1
                points[x2:x1 + 1, y2:y1 + 1] += 1
            elif x1 > x2 and y1 > y2:
                while x1 >= x2 and y1 >= y2:
                    points[x1, y1] += 1
                    x1 -= 1
                    y1 -= 1
            elif x1 < x2 and y1 < y2:
                while x1 <= x2 and y1 <= y2:
                    points[x1, y1] += 1
                    x1 += 1
                    y1 += 1
            elif x1 > x2 and y1 < y2:
                while x1 >= x2 and y1 <= y2:
                    points[x1, y1] += 1
                    x1 -= 1
                    y1 += 1
            elif x1 < x2 and y1 > y2:
                while x1 <= x2 and y1 >= y2:
                    points[x1, y1] += 1
                    x1 += 1
                    y1 -= 1

        result = np.sum(points >= 2)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve())
    print(sol.solve2())