# Player 1 starting position: 2
# Player 2 starting position: 5

# solution for dirac dice
import itertools
import functools

player1 = {'position': 2, 'score': 0, 'universe': 0}
player2 = {'position': 5, 'score': 0, 'universe': 0}
board = 10
win_score = 21
dice = [1, 2, 3]
turns = 0


def strategy_update(player, value):
    player['position'] += value
    player['position'] = player['position'] % board
    if player['position'] == 0:
        player['position'] = board

    player['score'] += player['position']


def strategy_rollback(player, value):
    player['score'] -= player['position']

    player['position'] -= value
    if player['position'] < 0:
        player['position'] = board + player['position']


def Game2(turns, count):
    if turns == 0:
        # player1 roll the dice
        count += 1
        if count == 3:
            turns = 1
            count = 0

            for value in dice:
                strategy_update(player1, value)

                if player1['score'] >= win_score:
                    player1['universe'] += 1
                else:
                    Game2(turns, count)

                strategy_rollback(player1, value)

        else:
            for value in dice:
                strategy_update(player1, value)

                Game2(turns, count)

                strategy_rollback(player1, value)

    elif turns == 1:
        # player2 roll the dice
        count += 1
        if count == 3:
            turns = 0
            count = 0

            for value in dice:
                strategy_update(player2, value)

                if player2['score'] >= win_score:
                    player2['universe'] += 1
                else:
                    Game2(turns, count)

                strategy_rollback(player2, value)

        else:
            for value in dice:
                strategy_update(player2, value)

                Game2(turns, count)

                strategy_rollback(player2, value)


@functools.lru_cache(maxsize=None)
def play(p1, s1, p2, s2):
    w1, w2 = 0, 0
    for m1, m2, m3 in itertools.product(dice, dice, dice):
        p1_copy = (p1 + m1 + m2 + m3) % board if (p1 + m1 + m2 + m3) % board else 10
        s1_copy = s1 + p1_copy
        if s1_copy >= win_score:
            w1 += 1
        else:
            w2_copy, w1_copy = play(p2, s2, p1_copy, s1_copy)
            w1 += w1_copy
            w2 += w2_copy

    return w1, w2


rf = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]


@functools.lru_cache(maxsize=None)
def wins(p1, t1, p2, t2):
    if t2 <= 0: return 0, 1

    w1,w2 = 0,0
    for (r,f) in rf:
        c2,c1 = wins(p2, t2, (p1+r)%10, t1 - 1 - (p1+r)%10) # remap 1-10 to 0-9
        w1,w2 = w1 + f * c1, w2 + f * c2

    return w1,w2


if __name__ == '__main__':
    Game2(turns, 0)
    print('Player1 wins in ',player1['universe'], 'universes')
    print('Player2 wins in ',player2['universe'], 'universes')
    print(max(play(2, 0, 5, 0)))
    print(max(wins(1, 21, 4, 21)))