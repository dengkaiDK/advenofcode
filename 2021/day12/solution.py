# Code Solution for day 12
# Time 2022-09-13


class Solution:
    def __init__(self):
        self.input = open('input.txt', 'r').read().splitlines()
        self.cave = list((row.split('-')[0], row.split('-')[1]) for row in self.input)
        self.connected_node = {}
        self.linked_node()

    def linked_node(self):
        for a, b in self.cave:
            if a not in self.connected_node:
                self.connected_node[a] = [b]
            else:
                self.connected_node[a].append(b)

            if b not in self.connected_node:
                self.connected_node[b] = [a]
            else:
                self.connected_node[b].append(a)

        return self.connected_node

    def run(self):
        paths = 0
        visited = []

        def DFS(node:str):
            nonlocal paths
            if node == 'end':
                paths += 1
                return

            if node.islower() and node in visited:
                return

            visited.append(node)
            for cave in self.connected_node[node]:
                if cave != 'start':
                    DFS(cave)
            visited.pop()
            return

        DFS('start')
        return paths

    def run2(self):
        paths = 0
        visited = []
        twice_cave = None

        def DFS(node:str):
            nonlocal paths
            nonlocal twice_cave

            if node == 'end':
                paths += 1
                return

            if node.islower() and twice_cave is not None and node in visited:
                return

            if node.islower() and twice_cave is None and node in visited:
                twice_cave = node

            visited.append(node)

            for cave in self.connected_node[node]:
                if cave != 'start':
                    DFS(cave)

            if node == twice_cave:
                twice_cave = None

            visited.pop()
            return

        DFS('start')
        return paths


if __name__ == '__main__':
    solution = Solution()
    print(solution.run())
    print(solution.run2())