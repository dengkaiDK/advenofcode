# code solution for day3
# Time 2022-09-04
from bitstring import BitArray, BitString
import numpy as np


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