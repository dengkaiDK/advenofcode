from itertools import product
from collections import defaultdict
import re


def default_factory():
    return False


cubes = defaultdict(default_factory)
on_count = 0


def parse_input():
    with open('input.txt') as f:
        return [line.strip() for line in f.readlines()]


def out_of_range(min, max):
    if min < -50 or max > 50:
        return True
    return False


def get_map(count, initial=True):
    lines = parse_input()
    pa = re.compile(r'(-?\d+)', re.IGNORECASE)
    for line in lines:
        coordinates = [int(x) for x in pa.findall(line)]
        if initial:
            if out_of_range(coordinates[0], coordinates[1]) \
                    or out_of_range(coordinates[2], coordinates[3]) \
                    or out_of_range(coordinates[4], coordinates[5]):
                print('out of range')
                break

        xrange = range(coordinates[0], coordinates[1] + 1)
        yrange = range(coordinates[2], coordinates[3] + 1)
        zrange = range(coordinates[4], coordinates[5] + 1)

        if re.match(r'on', line):
            for x, y, z in product(xrange, yrange, zrange):
                if (x, y, z) not in cubes:
                    cubes[(x, y, z)] = True
                    count += 1

        elif re.match(r'off', line):
            for x, y, z in product(xrange, yrange, zrange):
                if (x, y, z) in cubes:
                    del cubes[(x, y, z)]
                    count -= 1

        else:
            print('No matching regex')

    return count


def part1():
    global on_count
    print('Part 1')
    on_count = get_map(on_count)
    print(on_count)


if __name__ == '__main__':
    part1()
