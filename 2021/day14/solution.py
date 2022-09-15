# Code Solution for day14
# Time 2022-09-15
import copy


# define Linkedlist data structure
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def insert(self, val):
        node = LinkedList(val)
        node.next = self.next
        self.next = node
        return node.next


class Solution:
    def __init__(self):
        self.input = open('input.txt', 'r').read().splitlines()
        self.template = self.input[0]
        self.rules = []
        for i ,row in enumerate(self.input):
            if i > 1 and len(row) > 0:
                self.rules.append(tuple(row.strip().split(' -> ')))
        self.rules = dict(self.rules)
        # build Linkedlist
        head = LinkedList(' ')
        pointer = head
        for char in self.template:
            head.next = LinkedList(char)
            head = head.next

        self.polymer = pointer
        self.pair = {}

    def run(self):
        epoch = 10
        start = self.polymer.next
        # O(n * 2^epoch) drawback: only suitable when epoch is small
        for i in range(epoch):
            current = start
            while current.next is not None:
                pair_left = current.val
                pair_right = current.next.val
                pair = pair_left + pair_right
                if pair in self.rules:
                    current = current.insert(self.rules[pair])
                else:
                    current = current.next

        counter = {}
        current = start
        while current is not None:
            if current.val not in counter:
                counter[current.val] = 1
            else:
                counter[current.val] += 1
            current = current.next

        return max(counter.values()) - min(counter.values())

    def run2(self):
        epoch = 40

        for item in self.rules.keys():
            self.pair[item] = 0
        # O(k * epoch), compare to run(), this is much faster, k is the size of rules
        start = self.polymer.next
        current = start
        while current.next is not None:
            self.pair[current.val + current.next.val] += 1
            current = current.next

        for i in range(epoch):
            next_pair = copy.copy(self.pair)
            for item in self.pair.keys():
                left = item[0]
                right = item[1]
                mid = self.rules[item]
                next_pair[left + mid] += self.pair[item]
                next_pair[mid + right] += self.pair[item]
                next_pair[item] -= self.pair[item]
            self.pair = next_pair

        counter = {}
        for key, value in self.pair.items():
            if key[0] not in counter:
                counter[key[0]] = value
            else:
                counter[key[0]] += value
            if key[1] not in counter:
                counter[key[1]] = value
            else:
                counter[key[1]] += value

        counter['F'] += 1
        counter['B'] += 1

        return (max(counter.values()) - min(counter.values()))//2


if __name__ == '__main__':
    s = Solution()
    # print(s.run())
    print(s.run2()) # play with run2() or run() separately, because the linkedlist will be modified in run().
