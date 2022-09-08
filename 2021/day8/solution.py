# Code Solution for day8
# Time 2022-09-07

import numpy as np
import copy


class Solution:
    def __init__(self):
        self.input = open('input.txt', 'r').read().splitlines()
        self.signal = [row.split('|')[0].split() for row in self.input]
        self.output = [row.split('|')[1].split() for row in self.input]
        self.digits = {'0': set('a b c e f g'.split()), '1': set('c f'.split()), '2': set('a c d e g'.split()),
                  '3': set('a c d f g'.split()), '4': set('b c d f'.split()), '5': set('a b d f g'.split()),
                  '6': set('a b d e f g'.split()), '7': set('a c f'.split()), '8': set('a b c d e f g'.split()),
                  '9': set('a b c d f g'.split())}
        # print(len(self.signal))
        # print(len(self.output))

    def run1(self):
        cache = {'2': 0, '3': 0, '4': 0, '7': 0}
        for item in self.output:
            for i in item:
                if str(len(i)) in cache:
                    cache[str(len(i))] += 1
        return np.sum(list(cache.values()))

    def run2(self):
        code = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None}
        sum = 0
        for i in range(len(self.signal)):
            codemap = copy.copy(code)
            signal = self.signal[i]
            output = self.output[i]
            codelist = []
            for item in signal:
                key = set()
                strlen = len(item)
                for j in range(strlen):
                    key.add(item[j])
                codelist.append(key)
            codemap = self.findcode(codelist, codemap)
            # print(codemap)
            number = []
            for item in output:
                strlen = len(item)
                transform = set()
                for j in range(strlen):
                    transform.add(codemap[item[j]])
                number.extend([k for k, v in self.digits.items() if v == transform])
            sum += int(''.join(number))

        return sum


    def findcode(self, list, code):

        def getseven(list):
            length = 3
            return self.getcodebylen(list, length)

        def getone(list):
            length = 2
            return self.getcodebylen(list, length)

        def getfour(list):
            length = 4
            return self.getcodebylen(list, length)

        def geteight(list):
            length = 7
            return self.getcodebylen(list, length)

        one = getone(list)[0]
        seven = getseven(list)[0]
        four = getfour(list)[0]
        eight = geteight(list)[0]

        for item in seven:
            if item not in one:
                code[item] = 'a'

        for item in self.getcodebylen(list, 5):
            flag = 0
            for elem in seven:
                if elem not in item:
                    flag = 1
                    break

            if flag == 0:
                three = item
                break

        dg = set()
        for item in three:
            if item not in seven:
                dg.add(item)
        bd = set()
        for item in four:
            if item not in one:
                bd.add(item)

        for item in dg:
            if item in bd:
                code[item] = 'd'
            else:
                code[item] = 'g'

        for item in bd:
            if item not in dg:
                code[item] = 'b'

        for item in self.getcodebylen(list, 5):
            for elem in item:
                if code[elem] == 'b':
                    five = item
                    break

        for elem in five:
            if code[elem] is None:
                code[elem] = 'f'

        for elem in one:
            if code[elem] is None:
                code[elem] = 'c'

        for elem in eight:
            if code[elem] is None:
                code[elem] = 'e'

        return code

    def getcodebylen(self, list, length):
        result = []
        for item in list:
            if len(item) == length:
                result.append(item)

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.run1())
    print(sol.run2())
