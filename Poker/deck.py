from dataclasses import dataclass, field
import random
from typing import List
from card import Card, NAIPES, NUMEROS

@dataclass
class Deck(object):
    deck: List[Card] = field(default_factory=list)
    def __post_init__(self) -> None:
        self.deck = [Card(numero, naipe) for naipe in NAIPES for numero in NUMEROS]
    
    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def __len__(self) -> int:
        return len(self.deck)

    def deal(self) -> Card:
        return None if len(self) == 0 else self.deck.pop(0)