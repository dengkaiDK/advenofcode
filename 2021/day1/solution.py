# code solution for day 1
# Time: 2022-09-03
class solution:
    def __init__(self):
        self.input = open("input.txt", "r").read().splitlines()
        self.input = list(map(int, self.input))
        self.measurement = 0

    def solve(self):
        temp = self.input[0]
        for i in self.input:
            if i > temp:
                self.measurement += 1

            temp = i
        return self.measurement

    def reset(self):
        self.measurement = 0

    def solve2(self):
        temp = sum(self.input[:3])
        for j in range(1, len(self.input)-2):
            if temp < sum(self.input[j:j+3]):
                self.measurement += 1
            temp = sum(self.input[j:j+3])
        return self.measurement


if __name__ == "__main__":
    sol = solution()
    print(sol.solve())
    sol.reset()
    print(sol.solve2())