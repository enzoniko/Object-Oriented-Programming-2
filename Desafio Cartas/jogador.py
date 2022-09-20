from deck import Deck
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.hand = []

    def __str__(self):
        print(f'{self.nome} tem {len(self.hand)} cartas. Suas cartas são: ')
        return '\n'.join([str(card) for card in self.hand])
    
    
    def add_card(self, card):
        self.hand.append(card)

if __name__ == '__main__':
    jogadores = []
    deck = Deck().shuffle()
    for jogador in range(9):
        jogadores.append(Jogador(f'Jogador {jogador + 1}'))
        for _ in range(5):
            jogadores[jogador].add_card(deck.pop_card())

    for jogador in jogadores:
        print(jogador)


