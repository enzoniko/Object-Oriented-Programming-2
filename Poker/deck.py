import random
from card import Card

class Deck (object):
    def __init__ (self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank, suit)
                self.deck.append(card)

    def shuffle (self):
        random.shuffle (self.deck)

    def __len__ (self):
        return len (self.deck)

    def deal(self):
        return None if len(self) == 0 else self.deck.pop(0)