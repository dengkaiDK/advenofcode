# code solution for day 10
# Time 2022-09-11

import copy


class Solution:
    def __init__(self):
        self.input = open('input.txt', 'r').read().splitlines()
        self.score = {')': 3, ']': 57, '}': 1197, '>': 25137}

    def run(self):
        error_score = 0
        scores = []
        for row in self.input:
            stack = []
            corrupted = False
            score = 0
            for char in row:
                if len(stack) == 0:
                    stack.append(char)
                else:
                    if char not in self.score.keys():
                        stack.append(char)
                    else:
                        pop_char = stack.pop()
                        if pop_char == '(' and char != ')':
                            error_score += self.score[char]
                            corrupted = True
                        if pop_char == '[' and char != ']':
                            error_score += self.score[char]
                            corrupted = True
                        if pop_char == '{' and char != '}':
                            error_score += self.score[char]
                            corrupted = True
                        if pop_char == '<' and char != '>':
                            error_score += self.score[char]
                            corrupted = True

                if corrupted:
                    break

            if not corrupted and len(stack) > 0:
                while len(stack) > 0:
                    char = stack.pop()
                    score = 5 * score
                    if char == '(':
                        score += 1
                    if char == '[':
                        score += 2
                    if char == '{':
                        score += 3
                    if char == '<':
                        score += 4
                scores.append(score)

        scores = sorted(scores, reverse=False)
        middle_score = scores[len(scores) // 2]

        return error_score, middle_score


if __name__ == '__main__':
    sol = Solution()
    print(sol.run())