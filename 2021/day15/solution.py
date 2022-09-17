# Code Solution for day15
# Time 2022-09-17
import numpy as np
from heapq import heappush, heappop
from collections import defaultdict
import math
import time


class Solution:
    def __init__(self):
        self.input = open('input.txt', 'r').read().splitlines()
        self.risk_level = np.array([list(int(c) for c in string) for string in self.input])
        self.path_risk = np.zeros(self.risk_level.shape, dtype = np.int32)

    def part1(self):
        start = time.time()
        w, h = self.risk_level.shape # w == h is the condition
        # O(n^2) solution, but it has limitation that don't apply in part2. What if route has some up/left move ?
        path = 0
        # scan in diagonal
        while path < w + h - 2:
            path += 1
            if path < w:
                i = path
                j = 0
                while i >= 0:
                    if j == 0:
                        self.path_risk[i, j] = self.path_risk[i-1, j] + self.risk_level[i, j]
                    if i == 0:
                        self.path_risk[i, j] = self.path_risk[i, j-1] + self.risk_level[i, j]
                    if i > 0 and j > 0:
                        self.path_risk[i, j] = min(self.path_risk[i-1, j], self.path_risk[i, j-1]) + self.risk_level[i, j]
                    j += 1
                    i -= 1
            else:
                j = path - w + 1
                i  = w - 1
                while j < h:
                    self.path_risk[i, j] = min(self.path_risk[i, j-1], self.path_risk[i-1, j]) + self.risk_level[i, j]
                    j += 1
                    i -= 1

        time_collapsed = time.time() - start
        print('part 1 solution run {} minutes {} seconds'.format(int(time_collapsed // 60), int(time_collapsed % 60)))
        return self.path_risk[w-1, h-1]

    @staticmethod
    def find_neighbours(cell, w, h):
        i, j = cell
        out = []
        neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for neighbour in neighbours:
            if 0<= neighbour[0] < w and 0 <= neighbour[1] < h:
                out.append(neighbour)
        return out

    def part2(self):
        begin = time.time()
        full_map = np.tile(self.risk_level, (5, 5))
        path_risk = defaultdict(lambda: math.inf)
        w0, h0 = self.risk_level.shape
        w, h = full_map.shape
        # adjust new map
        for i in range(w):
            for j in range(h):
                full_map[i, j] = (full_map[i, j] + (i // w0) + (j // h0) - 1) % 9 + 1
        # implement priorty queue O(nlog(n)),  Dijiakstra algorithm, iterative suboptimal solution
        visited_cell = set()
        priority_queue = []
        start = (0, 0)
        end = (w-1, h-1)
        path_risk[start] = 0
        heappush(priority_queue, (0, start))
        while end not in path_risk:
            _, current = heappop(priority_queue)
            if current in visited_cell:
                continue
            neighbours = Solution().find_neighbours(current, w, h)
            for neighbour in neighbours:
                if neighbour in visited_cell:
                    continue
                path_risk[neighbour] = min(path_risk[neighbour], path_risk[current] + full_map[neighbour])
                heappush(priority_queue, (path_risk[neighbour], neighbour))
            visited_cell.add(current)
        time_collapsed = time.time() - begin
        print('part 2 solution run {} minutes {} seconds'.format(int(time_collapsed // 60), int(time_collapsed % 60)))
        return path_risk[end]


if __name__ == '__main__':
    solution = Solution()
    print(solution.part1())
    print(solution.part2())