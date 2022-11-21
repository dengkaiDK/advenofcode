import numpy as np
from collections import defaultdict
from itertools import combinations
from utils import Rotations


class Solution:
    def __init__(self, input):
        self.input = open(input, 'r').read().splitlines()
        self.scanner = {}
        self.build()

    def build(self):
        count = 0
        for line in self.input:
            if line == '--- scanner %d ---'%count:
                self.scanner[count] = []
                count += 1
                continue
            if line == '':
                continue

            temp = tuple(map(int, line.split(',')))
            self.scanner[count-1].append(temp)

    def distance(self, a, b):
        return sum((x - y)**2 for x, y in zip(a, b))

    # using distance as an approximmation of similarity
    def pairwise_distance(self, scanner):
        return [[self.distance(a, b) for a, b in combinations(s, 2)] for s in scanner]

    def findoverlapping(self, scanner):
        overlapping = defaultdict(list)
        distance = self.pairwise_distance(scanner)
        for i, j in combinations(range(len(scanner)), 2):
            d1 = distance[i]
            d2 = distance[j]
            common = list(set(d1).intersection(d2))
            if len(common) >= 66:
                overlapping[i].append(j)
                overlapping[j].append(i)
        return overlapping

    # key compnents
    def findCommonBeacons(self, beacons1, beacons2, verbose=True):
        c1 = [(a, b) for a, b in combinations(beacons1, 2)]
        c2 = [(a, b) for a, b in combinations(beacons2, 2)]
        d1 = [self.distance(a, b) for a, b in combinations(beacons1, 2)]
        d2 = [self.distance(a, b) for a, b in combinations(beacons2, 2)]
        common = list(set(d1).intersection(set(d2)))
        if len(common) >= 66:
            if verbose: print("Found overlapping region ", end="")
            C1 = []
            C2 = []
            for c in common:
                i1 = d1.index(c)
                i2 = d2.index(c)
                for x1 in c1[i1]:
                    if x1 not in C1:
                        C1.append(x1)
                for x2 in c2[i2]:
                    if x2 not in C2:
                        C2.append(x2)
            if verbose: print("with {} common beacons.".format(len(C1)))
            if verbose: print("Looking for rotation and scanner distance... ", end="")
            # Taking one point as reference
            X1 = np.array(C1[0])
            R = None
            dX = None
            # Trying all points in corresponding set to find match
            matchFound = False
            for x2 in C2:
                X2 = np.array(x2)
                # Trying all rotations
                for R in Rotations:
                    X2rot = np.matmul(R, X2)
                    # Translation between reference point X1 and test point X2 after rotation
                    dX = X1 - X2rot
                    # If point and rotation correct, than all other points should have a correspondence in original set
                    C2transf = [tuple(np.matmul(R, np.array(x2t)) + dX) for x2t in C2]
                    inOriginal = [1 for x2t in C2transf if x2t in C1]
                    # There might be more than 12 elements in C1 for spurious matching of
                    # distances, only check for lenght of inOriginal to be at least 12
                    # if len(inOriginal)==len(C1):
                    if len(inOriginal) >= 12:
                        if verbose: print("found!")
                        if verbose: print(R, dX)
                        matchFound = True
                        break
                if matchFound: break
            if not matchFound:
                return [], (0, 0, 0)
            if verbose: print("Translating all points in second set to coordinate of first set... ", end="")
            beacon2new = [tuple(np.matmul(R, np.array(x2)) + dX) for x2 in beacons2]
            if verbose: print("Done.")
            return beacon2new, tuple(dX)
        else:
            if verbose: print("No overlapping region found.")
            return [], (0, 0, 0)

    def part1(self):
        # print(self.scanner[0])
        # find similar child matrix inside each matrix
        scanner = self.scanner
        scanner_new = [[]] * len(scanner)
        scanner_new[0] = list(scanner[0])
        scanner_coord = [(0, 0, 0)] * len(scanner)
        translated = [0]
        refs = [0]
        while len(translated) < len(scanner):
            iref = refs.pop()
            b1 = scanner_new[iref]
            for i in range(len(scanner)):
                if i != iref and i not in translated:
                    b2 = scanner[i]
                    b2new, Xscanner = self.findCommonBeacons(b1, b2, verbose=False)
                    if len(b2new):
                        scanner_new[i] = b2new
                        scanner_coord[i] = Xscanner
                        translated.append(i)
                        refs.append(i)
        return scanner_new, scanner_coord

    def manhattanDistance(a, b):
        return sum([abs(xa - xb) for xa, xb in zip(a, b)])

    def part2(self, scanner_coord):
        return max([Solution.manhattanDistance(a, b) for a, b in combinations(scanner_coord, 2)])


def part1(scanner_new):
    overlap = set([])
    for b in scanner_new:
        overlap = overlap | set(b)
    return len(overlap)


if __name__ == '__main__':
    s = Solution('input.txt')
    scanner_new, scanner_coord= s.part1()
    print("part1:", part1(scanner_new))
    print("part2:", s.part2(scanner_coord))
