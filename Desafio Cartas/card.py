class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        suits = ['Paus', 'Ouros', 'Copas', 'Espadas']
        ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei']
        return f'{ranks[self.rank]} de {suits[self.suit]}'
    
