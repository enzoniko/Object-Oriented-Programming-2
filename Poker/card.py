from dataclasses import dataclass
from typing import List

NUMEROS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
NAIPES = ('S', 'D', 'H', 'C')

def print_hand(label: str, hand: List[str]) -> None:
  print(label)
  print('\n'.join(map('  '.join, zip(*(make_card(c) for c in hand)))))

def make_card(name: str) -> List[str]:
  carta = [
      "┌─────────┐", "│{}{}. . .│", "│. . . . .│", "│. . . . .│",
      "│. . {}. .│", "│. . . . .│", "│. . . . .│", "│. . .{}{}│", "└─────────┘"
  ]
  x = ("│.", name[0], ". . . .│")
  carta[1] = "".join(x)

  x = ("│. . . .", name[0], ".│")
  carta[7] = "".join(x)

  if "D" in name:
    carta[4] = "│. . ♦ . .│"
  if "C" in name:
    carta[4] = "│. . ♣ . .│"
  if "H" in name:
    carta[4] = "│. . ♥ . .│"
  if "S" in name:
    carta[4] = "│. . ♠ . .│"

  return carta

@dataclass
class Card(object):
  rank: int = 0
  suit: str = ''

  def __str__(self) -> str:
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return f'{rank}{self.suit}'

  def __eq__(self, other: object) -> bool:
    return (self.rank == other.rank)

  def __ne__(self, other: object) -> bool:
    return (self.rank != other.rank)

  def __lt__(self, other: object) -> bool:
    return (self.rank < other.rank)

  def __le__(self, other: object) -> bool:
    return (self.rank <= other.rank)

  def __gt__(self, other: object) -> bool:
    return (self.rank > other.rank)

  def __ge__(self, other) -> bool:
    return (self.rank >= other.rank)