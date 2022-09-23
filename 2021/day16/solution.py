# Code Solution for day 16
# Time 2022-09-19
from icecream import ic


ic.configureOutput(includeContext=True)


class Solution:
    def __init__(self):
        self.hexadecimal = open('input.txt', 'r').read().splitlines()[0]
        self.map_table = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                          '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                          'E': '1110', 'F': '1111'}
        self.bitarray = list(map(lambda x: self.map_table[x], self.hexadecimal))
        self.bitstring = ''.join(self.bitarray)
        self.type = {0: 'sum', 1: 'product', 2: 'minimum', 3: 'maximum', 5: '>', 6: '<', 7: '='}

    def calculate(self, operator, val: list):
        if operator == 'sum':
            return sum(val)
        elif operator == 'product':
            product = 1
            for v in val:
                product *= v
            return product
        elif operator == 'minimum':
            return min(val)
        elif operator == 'maximum':
            return max(val)
        elif operator == '>':
            return val[0] > val[1]
        elif operator == '<':
            return val[0] < val[1]
        elif operator == '=':
            return val[0] == val[1]

    def run(self):
        version_sum = 0
        read = 'version'
        packet_stack = []
        numeric = ''
        i = 0  # index
        while i < len(self.bitstring):
            if read == 'version':
                version_sum += int(self.bitstring[i:i + 3], 2)
                i += 3
                read = 'type'
            elif read == 'type':
                packet_type = int(self.bitstring[i:i+3], 2)
                i += 3
                if packet_type == 4:
                    read = 'value'
                    numeric = ''
                else:
                    read = 'operator'
            elif read == 'operator':
                length_type = self.bitstring[i]
                i += 1
                if length_type == '0':
                    length = int(self.bitstring[i:i+15], 2)
                    i += 15
                    packet_stack.append({'type': length_type, 'length': length, 'start': i,
                                         'operator': self.type[packet_type], 'value': []})
                else:
                    length = int(self.bitstring[i:i+11], 2)
                    i += 11
                    packet_stack.append({'type': length_type, 'length': length, 'number': 0,
                                         'operator': self.type[packet_type], 'value': []})
                read = 'version'  # sub-packet

            elif read == 'value':
                flag = self.bitstring[i]
                i += 1
                while flag != '0':
                    numeric += self.bitstring[i:i + 4]
                    i += 4
                    flag = self.bitstring[i]
                    i += 1
                numeric += self.bitstring[i:i + 4]
                i += 4
                number = int(numeric, 2)
                finished = True  # check if all sub-packets are finished
                while finished and len(packet_stack) > 0:
                    parent = packet_stack[-1]
                    parent['value'].append(number)
                    if parent['type'] == '0':
                        if parent['start'] + parent['length'] == i:
                            calculator = packet_stack.pop()
                            number = self.calculate(calculator['operator'], calculator['value'])
                        else:
                            finished = False
                    if parent['type'] == '1':
                        parent['number'] += 1
                        if parent['number'] == parent['length']:
                            calculator = packet_stack.pop()
                            number = self.calculate(calculator['operator'], calculator['value'])
                        else:
                            finished = False
                # ic(number)
                read = 'version'

        return version_sum, number


if __name__ == "__main__":
    solution = Solution()
    version, value = solution.run()
    print('Version sum: {}, Expression value: {}'.format(version, value))
