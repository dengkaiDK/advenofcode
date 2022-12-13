# adventofcode day 24

from time import perf_counter as pfc


def read_puzzle(filename):
    with open(filename) as f:
        return [row.split() for row in f.read().split("\n") if len(row) > 0]


def get_relevant_adds(puzzle):
    div1, div26 = [], []
    for i in range(0, len(puzzle), 18):
        if puzzle[i + 4][2] == "1":
            div1.append(int(puzzle[i + 15][2]))
            div26.append(None)
        else:
            div1.append(None)
            div26.append(int(puzzle[i + 5][2]))
    return div1, div26


def get_model_no(div1, div26, part1):
    modelNo = [0] * 14
    stack = []
    startDigit = 9 if part1 else 1
    for i, (a, b) in enumerate(zip(div1, div26)):
        if a:
            stack.append((i, a))
        else:
            ia, a = stack.pop()
            diff = a + b
            if part1:
                modelNo[ia] = min(startDigit, startDigit - diff)
                modelNo[i] = min(startDigit, startDigit + diff)
            else:
                modelNo[ia] = max(startDigit, startDigit - diff)
                modelNo[i] = max(startDigit, startDigit + diff)
    return modelNo


def solve(puzzle, part1=True):
    div1, div26 = get_relevant_adds(puzzle)
    return "".join(map(str, get_model_no(div1, div26, part1)))


start = pfc()
print(solve(read_puzzle("day24/input.txt")))
print(solve(read_puzzle("day24/input.txt"), False))
print(pfc() - start)