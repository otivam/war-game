import random

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self,suite,ranks):
        self.suite = suite
        self.ranks = ranks

    deck = []
    half_1 = []
    half_2 = []

    for x in SUITE:
        for y in RANKS:
            deck.append(x+y)

    def shuffle(self):
        random.shuffle(self.deck)   

    def cut(self):
        middle_index = len(self.deck)//2
        self.half_1 = self.deck[:middle_index]
        self.half_2 = self.deck[middle_index:]


class Hand:
    def __init__(self,hand):
        self.hand = hand

    def add(self,card):
        self.hand.append(card)

    def remove(self):
        self.hand.pop()


class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play(self):
        drawn_card = self.hand.remove()
        print("{} has placed {}".format(self.name,drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        for x in range(3):
            war_cards.append.self.hand.remove()

        return war_cards

    def __len__(self):
        return len(self.hand)



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

game_on = True

while game_on:
    new_deck = Deck(SUITE,RANKS)
    new_deck.shuffle()
    new_deck.cut()

    print("Player 1 name: ")
    player1_name = input()
    print("Hello {} !".format(player1_name))
    player1 = Player(player1_name,new_deck.half_1)

    print("Player 2 name: ")
    player2_name = input()
    print("Hello {}".format(player2_name))
    player2 = Player(player2_name,new_deck.half_2)
