# Solution for day 20 in 2021 adventof code
# https://adventofcode.com/2021/day/20

# clues:
# image enhancement string, length: 512
# rule : in order to get a output image from input image
# we need to apply some transform to every basic pixels of input image
# First, a 3 * 3 grid need to be considered as a unit
# convert the unit to a number, and use the number as index in image enhancement string to get the output pixel.
# In the first part, we need to repeat the process twice.
# what we need to be careful is to consider the edge case. Because the input image is infinite.

from collections import defaultdict

char_to_bit ={'#': 1, '.': 0}
edge_char = '.'


def defaultstr():
    return edge_char


def alter():
    global edge_char
    if edge_char == '.':
        edge_char = '#'
    else:
        edge_char = '.'


def get_input():
    input_image = defaultdict(defaultstr)

    with open('input.txt') as f:
        lines = f.readlines()
        image_enhancement = list([x for x in lines[0].strip()])
        print(len(lines[2:]))
        for i, line in enumerate(lines[2:]):
            if i == 0: print(len(line.strip()))
            for j, char in enumerate(line.strip()):
                input_image[(i, j)] = char

    return image_enhancement, input_image


def get_index(image, i, j):
    unit = ''
    try:
        for x in range(-1, 2):
            for y in range(-1, 2):
                # consider infinite cases
                unit += str(char_to_bit[image[(i + x, j + y)]])
    except KeyError:
        print('key error', 'i+x', i+x, 'j+y', j+y)
        raise KeyError
    else:
        return int(unit, 2)


image_enhancement, input_image = get_input()

# unit test
def unittest1():
    assert image_enhancement[get_index(input_image, 0, 0)] == 1  # 全0输出1
    assert image_enhancement[get_index(input_image, -100, -100)] == 1
    assert image_enhancement[get_index(input_image, 32, 1)] == 0  # 全1输出0

def test():
    unittest1()

# 第一轮处理，考虑范围为{(-1, -1), (-1, 100), (100, -1), (100, 100)}   input_image大小为100 * 100
# 第二轮处理，考虑范围为{(-2, -2), (-2, 101), (101, -2), (101, 101)}   input_image大小为102 * 102


top_left = (0, 0)
down_right = (100, 100)


def get_output_image(epoch, input_image, tl, dr):

    for e in range(epoch):
        output_image = image_process(input_image, tl, dr)
        tl = (tl[0] - 1, tl[1] - 1)
        dr = (dr[0] + 1, dr[1] + 1)
        input_image = output_image

    return output_image, tl, dr


def image_process(input_image, tl, dr):
    output_image = defaultdict(defaultstr)
    for i in range(tl[0] - 1, dr[0] + 1):
        for j in range(tl[1] -1, dr[1] + 1):
            output_image[(i, j)] = image_enhancement[get_index(input_image, i, j)]
    alter()
    return output_image


def part12(top_left, down_right, epoch):
    output_image, top_left, down_right = get_output_image(epoch, input_image, top_left, down_right)
    count = 0
    for i in range(top_left[0], down_right[0]):
        for j in range(top_left[1], down_right[1]):
            if output_image[(i, j)] == '#':
                count += 1

    return count


print(part12(top_left, down_right, 2))  # part 1
print(part12(top_left, down_right, 50))  # part 2
