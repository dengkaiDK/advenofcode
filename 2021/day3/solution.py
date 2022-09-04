# code solution for day3
# Time 2022-09-04
from bitstring import BitArray
import numpy as np
import copy


class Solution:
    def __init__(self):
        self.input = open("input.txt", "r").read().splitlines()
        self.input = list(map(lambda x: list(x), self.input))
        self.input = np.array(self.input)

    def solve(self):
        n, l = self.input.shape
        result = []
        for i in range(0, l):
            if np.sum(self.input[:,i] == '1') > n / 2:
                result.append(1)
            else:
                result.append(0)

        return result

    def solve2_oxygen(self):
        n, l = self.input.shape
        position = 0
        remain = n
        report = copy.copy(self.input)
        while remain > 1:
            mask = report[:, position] == '1'
            if np.sum(mask) >= remain / 2:
                report = report[mask, :]
                remain = np.sum(mask)
            else:
                report = report[~mask, :]
                remain = np.sum(~mask)
            position += 1
            if position >= l:
                position = 0

        return np.squeeze(report, axis=0).tolist()

    def reset(self):
        self.input = open("input.txt", "r").read().splitlines()
        self.input = list(map(lambda x: list(x), self.input))
        self.input = np.array(self.input)

    def solve2_co2(self):
        n, l = self.input.shape
        position = 0
        remain = n
        report = copy.copy(self.input)
        while remain > 1:
            mask = report[:, position] == '0'
            if np.sum(mask) <= remain / 2:
                report = report[mask, :]
                remain = np.sum(mask)
            else:
                report = report[~mask, :]
                remain = np.sum(~mask)
            position += 1
            if position >= l:
                position = 0

        return np.squeeze(report, axis=0).tolist()


if __name__ == "__main__":
    sol = Solution()
    rel = sol.solve()
    # print(rel) # list [int]
    rel = BitArray(rel) # Bitarray
    # print(rel) # Bitarray hex
    # print(rel.bin) # base2 str
    # print(type(rel.bin)) #str
    gamma, ep = int(rel.bin, 2), int((~rel).bin, 2)
    print(gamma * ep)
    oxygen = sol.solve2_oxygen()
    # sol.reset()
    co2 = sol.solve2_co2()
    oxygen, co2 =[int(x) for x in oxygen], [int(x) for x in co2]
    oxygen, co2 = BitArray(oxygen), BitArray(co2)
    # print(oxygen.bin, co2.bin)
    oxygen, co2 = int(oxygen.bin, 2), int(co2.bin, 2)
    print(oxygen * co2)
