# solution for day 21

# Player 1 starting position: 2
# Player 2 starting position: 5


class Die:
    def __init__(self, sides=100):
        self.sides = sides
        self.value = 1
        self.count = 0

    def roll(self):
        self.update()
        ans = self.value
        if self.value < self.sides:
            self.value += 1
        else:
            self.value = 1
        return ans

    def update(self):
        self.count += 1

    def get_count(self):
        return self.count


class Player:
    def __init__(self, position, score=0):
        self.position = position
        self.score = score

    def win(self):
        if self.score >= 1000:
            return True
        return False

    def move(self, die: Die, board: int):
        result = 0
        for _ in range(3):
            result += die.roll()

        self.position += result
        self.position = self.position % board
        if self.position == 0:
            self.position = board

        self.score += self.position

    def get_score(self):
        return self.score


class Game:
    def __init__(self, board=10):
        self.board = board
        self.die = Die()
        self.player1 = Player(2)
        self.player2 = Player(5)
        self.end = False
        self.part1 = 0

    def play(self):
        while not self.end:
            self.player1.move(self.die, self.board)
            if self.player1.win():
                self.end = True
                self.part1 = self.die.get_count() * self.player2.get_score()
                break
            self.player2.move(self.die, self.board)
            if self.player2.win():
                self.end = True
                self.part1 = self.die.get_count() * self.player1.get_score()
                break

        return self.part1




def main():
    game = Game()
    print(game.play())


if __name__ == '__main__':
    main()