# code Solution for day 2
# Time 2022-09-04

class Solution:
    def __init__(self):
        self.input = open("input.txt", "r").read().splitlines()
        self.input = list(map(lambda x: x.split(" "), self.input))
        self.horizon = 0
        self.depth = 0
        self.aim = 0

    def solve(self):
        for i in range(0, len(self.input)):
            if self.input[i][0] == 'forward':
                self.horizon += int(self.input[i][1])
            if self.input[i][0] == 'down':
                self.depth += int(self.input[i][1])
            if self.input[i][0] == 'up':
                self.depth -= int(self.input[i][1])
        return self.horizon, self.depth

    def reset(self):
        self.horizon = 0
        self.depth = 0
        self.aim = 0

    def solve2(self):
        for j in range(0, len(self.input)):
            if self.input[j][0] == 'forward':
                self.horizon += int(self.input[j][1])
                self.depth += int(self.input[j][1]) * self.aim
            if self.input[j][0] == 'down':
                self.aim += int(self.input[j][1])
            if self.input[j][0] == 'up':
                self.aim -= int(self.input[j][1])

        return self.horizon, self.depth


if __name__ == "__main__":
    sol = Solution()
    h, d = sol.solve()
    print(h*d)
    sol.reset()
    h, d = sol.solve2()
    print(h*d)
