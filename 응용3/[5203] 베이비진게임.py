import sys
sys.stdin = open('5203input.txt')

class Deck:
    def __init__(self):
        self.deck = {}

    def insert(self, card):
        deck = self.deck
        if card in deck:
            if deck[card] >= 2:
                return True
            else:
                deck[card] += 1
        else:
            deck[card] = 1
            if self.is_run(card):
                return True
        return False

    def is_run(self, card):
        deck = self.deck
        if card-1 in deck:
            if card-2 in deck or card+1 in deck:
                return True
        elif card+1 in deck:
            if card+2 in deck or card-1 in deck:
                return True
        return False

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))

    player_one = Deck()
    player_two = Deck()
    answer = 0

    for i in range(len(data)):
        if i%2:
            if player_two.insert(data[i]):
                answer = 2
                break
        else:
            if player_one.insert(data[i]):
                answer = 1
                break
    print('#{} {}'.format(tc, answer))