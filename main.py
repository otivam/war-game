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
    halfs = []

    for x in SUITE:
        for y in RANKS:
            deck.append(x+y)

    def shuffle(self):
        random.shuffle(self.deck)   

    def cut(self):
        middle_index = len(self.deck)//2
        self.half_1 = self.deck[:middle_index]
        self.half_2 = self.deck[middle_index:]
        self.halfs = [self.half_1,self.half_2]

class Hand:
    def __init__(self,cards):
        self.cards = cards

    def add(self,card):
        self.cards.extend(card)

    def remove(self):
        return self.cards.pop()


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
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove())
            return war_cards

    def __len__(self):
        return len(self.hand.cards)



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

new_deck = Deck(SUITE,RANKS)
new_deck.shuffle()
new_deck.cut()

my_data = {}
def generate_players(num_of_players):
    for x in range(num_of_players):
        print("Player {} name: ".format(x+1))
        my_data['player{}_name'.format(x+1)] = input() 
        print("Hello {} !".format(my_data['player{}_name'.format(x+1)]))
        my_data['player{}'.format(x+1)] = Player(my_data['player{}_name'.format(x+1)],Hand(new_deck.halfs[x]))


generate_players(2)

player1 = my_data['player1']
player2 = my_data['player2']


count_rounds = 0
count_wars = 0

def small_battle_check_condition():
    if RANKS.index(p1_played_card[1:]) < RANKS.index(p2_played_card[1:]):
        print('{} win, adding {} cards to hand.'.format(player2.name,len(cards_on_table)))
        player2.hand.add(cards_on_table)
    else:
        print('{} win, adding {} cards to hand.'.format(player1.name,len(cards_on_table)))
        player1.hand.add(cards_on_table)



while len(player1.hand.cards) > 0 and len(player2.hand.cards) > 0:
    count_rounds += 1
    cards_on_table = []

    print('New round! {}'.format(count_rounds))
    print('Current standings:')
    print('{} cards count: {}'.format(player1.name,len(player1.hand.cards)))
    print('{} cards count: {}'.format(player2.name,len(player2.hand.cards)))

    p1_played_card = player1.play()
    p2_played_card = player2.play()

    cards_on_table.append(p1_played_card)
    cards_on_table.append(p2_played_card)


    if p1_played_card[1:] == p2_played_card[1:]:
        print('WAR!')
        print("Each player removes 3 cards 'face down' and then one card face up")
        count_wars += 1

        cards_on_table.extend(player1.remove_war_cards())
        cards_on_table.extend(player2.remove_war_cards())

        if len(player1.hand.cards) > 0 and len(player2.hand.cards) > 0:
            p1_played_card = player1.play()
            p2_played_card = player2.play()

            cards_on_table.append(p1_played_card)
            cards_on_table.append(p2_played_card)

            small_battle_check_condition()

    else:
        small_battle_check_condition()

if len(player1.hand.cards) == 0:
    print('{} win!'.format(player2.name))
else:
    print('{} win!'.format(player1.name))

print("Great Game, it lasted: {}".format(count_rounds))
print("A war occured {} times".format(count_wars))
