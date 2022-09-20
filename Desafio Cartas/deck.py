import itertools
import random
from card import Card
class Deck:
    def __init__(self):
        self.cards = []
        for suit, rank in itertools.product(range(4), range(1, 14)):
            card = Card(suit, rank)
            self.cards.append(card)
            
    def __str__(self):
        res = [str(card) for card in self.cards]
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)

