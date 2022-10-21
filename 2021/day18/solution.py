# Code Solution for day 18
#Time 2022-09-28
from ast import literal_eval


# define basic tree data structure
class snailfish:
    def __init__(self, data=-1, level = 0, pair=False):
        self.data = data
        self.level = level
        self.pair = pair
        self.left = None
        self.right = None
        self.parent = None

    def add_leftchild(self, data= -1, level=0, pair= False):
        self.left = snailfish(data, level, pair)
        self.left.parent = self

    def add_rightchild(self, data= -1, level=0, pair= False):
        self.right = snailfish(data, level,  pair)
        self.right.parent = self

    def add_leftnode(self, node):
        self.left = node
        self.left.parent = self

    def add_rightnode(self, node):
        self.right = node
        self.right.parent = self

    def get_data(self):
        return self.data

    def get_level(self):
        return self.level

    def is_pair(self):
        return self.pair


class Solution:
    def __init__(self, file):
        self.input = open(file, 'r').read().splitlines()
        self.numbers = [literal_eval(line) for line in self.input]

    @staticmethod
    def build_tree(number):
        root = snailfish(level=0,pair=True)
        queue = [(root, number)]
        while len(queue) > 0:
            current, number = queue.pop(0)
            left, right = number
            if isinstance(left, int):
                current.add_leftchild(data=left, level=current.level+1, pair=False)
            else:
                current.add_leftchild(data=-1, level=current.level+1, pair=True)
                queue.append((current.left, left))
            if isinstance(right, int):
                current.add_rightchild(data=right, level=current.level+1, pair=False)
            else:
                current.add_rightchild(data=-1, level=current.level+1, pair=True)
                queue.append((current.right, right))
        return root

    @staticmethod
    def addition(root1, root2):
        root = snailfish(level=0,pair=True)
        root.add_leftnode(root1)
        root.add_rightnode(root2)
        queue = [root]
        # update level
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is not None:
                current.left.level = current.level + 1
                queue.append(current.left)
            if current.right is not None:
                current.right.level = current.level + 1
                queue.append(current.right)
        return root

    @staticmethod
    def explode(node: snailfish):
        # explosion of one node
        assert node.left.pair is False
        assert node.right.pair is False
        left_value, right_value = node.left.data, node.right.data
        node.pair = False
        node.data = 0
        node.left.parent = None
        node.right.parent = None
        node.left = None
        node.right = None

        current = node
        parent = node.parent
        # update left_value, right_value
        if parent:
            while parent.left == node:
                node = parent
                parent = node.parent
                if parent is None:
                    break

        if parent is not None:
            node = parent.left
            # find rightmost node
            while node.pair:
                node = node.right
            node.data += left_value

        node = current
        parent = node.parent
        if parent:
            while parent.right == node:
                node = parent
                parent = node.parent
                if parent is None:
                    break

        if parent is not None:
            node = parent.right
            # find leftmost node
            while node.pair:
                node = node.left
            node.data += right_value

    @staticmethod
    def split(node: snailfish):
        # split of one node
        assert node.pair is False
        left_value, right_value = node.data // 2, node.data - node.data // 2
        node.pair = True
        node.data = -1
        node.add_leftchild(left_value, node.level + 1, False)
        node.add_rightchild(right_value, node.level + 1, False)

    @staticmethod
    def print_tree(root: snailfish):
        queue = [root]
        # print tree in BFS
        print('Tree result in BFS')
        while len(queue)>0:
            current = queue.pop(0)
            if current.pair:
                print('Pair  {}'.format(current.level), end=' ,')
            else:
                print('Data {}:'.format(current.level), current.data, end=' ,')
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        print()

    @staticmethod
    def lmr_explode(root: snailfish):
        if root.left.is_pair():
            if Solution.lmr_explode(root.left):
                return True
        # first check if apply to explode
        if root.is_pair():
            if root.level >= 4:
                #print('Explode node: [{}, {}] at level {}'.format(root.left.data, root.right.data, root.level))
                Solution.explode(root)
                return True

        if root.right.is_pair():
            if Solution.lmr_explode(root.right):
                return True

    @staticmethod
    def lmr_split(root:snailfish):
        if root.left is not None:
            if Solution.lmr_split(root.left):
                return True

        if root.is_pair() is False:
            if root.data >= 10:
                Solution.split(root)
                return True

        if root.right is not None:
            if Solution.lmr_split(root.right):
                return True

    @staticmethod
    def magnitude(root):
        if not root.pair:
            return root.data
        else:
            return 3 * Solution.magnitude(root.left) + 2 * Solution.magnitude(root.right)

    def part1(self):
        # lmr traversal in tree
        left = None
        for number in self.numbers:
            if left is None:
                left = self.build_tree(number)
                continue
            right = self.build_tree(number)
            root = self.addition(left, right)
            # reduce process
            while True:
                # first check all the exploding condition
                flag = None
                while self.lmr_explode(root) is not None:
                    pass
                #then check if exists any splitting condition
                flag = self.lmr_split(root)
                if flag is None:
                    break
            left = root
            # print('After update')
            # Solution.print_tree(root)

        return Solution.magnitude(root)

    def reduce(self, left: snailfish, right: snailfish):
        lr = self.addition(left, right)

        while True:
            flag = None
            while self.lmr_explode(lr) is not None:
                pass

            flag = self.lmr_split(lr)
            if flag is None:
                break

        return lr

    def part2(self):
        magnitude = 0
        # O(n^2)
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if i == j:
                    continue
                left = self.build_tree(self.numbers[i])
                right = self.build_tree(self.numbers[j])
                result= self.reduce(left, right)
                magnitude = max(magnitude, Solution.magnitude(result))

        return magnitude


if __name__ == "__main__":
    s = Solution('input.txt')
    print(s.part1())
    print(s.part2())
