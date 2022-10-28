from dataclasses import dataclass, field
from typing import List
from deck import Deck
from card import Card, print_hand

@ dataclass
class Poker(object):
    deck: Deck = field(default_factory=Deck)
    hands: List[List[Card]] = field(default_factory=list)
    tlist: list = field(default_factory=list)
    num_hands: int = 0
    num_cards_in_hand: int = 5

    def __post_init__(self) -> None:
        # Distribui as cartas para cada mão
        self.deck.shuffle()
        for _ in range(self.num_hands):
            self.hands.append([self.deck.deal() for _ in range(self.num_cards_in_hand)])
      
    def play(self) -> None:
        # Printa as mãos
        for i, hand in enumerate(self.hands):
            print_hand(f' Mão do Jogador {str(i + 1)}:', [str(card) for card in sorted(hand, reverse = True)])
            print('----------------------------------------------------------------')
                
    def point(self, hand: List[Card]) -> int: 
        # Calcula pontuação parcial
        return sum(rank * 13 ** i for i, rank in enumerate(card.rank for card in hand))
       
    def isRoyal(self, hand, flag: bool = True) -> None: 
        # Printa 'Royal Flush' se for verdadeiro, se não, passa para isStraightFlush(hand)
        sortedHand: List[Card] = sorted(hand, reverse = True)
        Currank: int = 14
        for card in sortedHand:
            if card.suit != sortedHand[0].suit or card.rank != Currank:
                flag: bool = False
                break
            else:
                Currank -= 1
        if flag:
            print('Royal Flush')
            self.tlist.append(10 * 13 ** 5 + self.point(sortedHand))    
        else:
            self.isStraightFlush(sortedHand)
        

    def isStraightFlush(self, hand, flag: bool = True) -> None:   
        # Printa 'Straight Flush' se for verdadeiro, se não, passa para isFour(hand)   
        Currank: int = hand[0].rank
        for card in hand:
            if card.suit != hand[0].suit or card.rank != Currank:
                flag: bool = False
                break
            else:
                Currank -= 1
        if flag:
            print('Straight Flush')
            self.tlist.append(9 * 13 ** 5 + self.point(hand))
        else:
            self.isFour(hand)

    def isFour(self, hand) -> None:     
        # Printa 'Four of a Kind' se for verdadeiro, se não, passa para isFull(hand)
        # Como tem 4 cartas iguais, a segunda na lista ordenada tem que ser a carta que se repete
        if sum(card.rank == hand[1].rank for card in hand) >= 4:
            print('Quadra')
            self.tlist.append(8 * 13 ** 5 + self.point(hand))
        else:
            self.isFull(hand)
        
    def isFull(self, hand) -> None:       
        # Printa 'Full House' se for verdadeiro, se não, passa para isFlush(hand) 
        # A primeira e a última carta da lista ordenada tem que ser diferentes em uma lista ordenada                    
        num_rank1: int = [card.rank for card in hand].count(hand[0].rank)
        num_rank2: int = [card.rank for card in hand].count(hand[-1].rank)
        if (num_rank1 == 2 and num_rank2 == 3) or (num_rank1 == 3 and num_rank2 == 2):
            print('Full House')
            self.tlist.append(7 * 13 ** 5 + self.point(hand))
        else:
            self.isFlush(hand)

    def isFlush(self, hand) -> None:   
        # Printa 'Flush' se for verdadeiro, se não, passa para isStraight(hand)              
        if all(card.suit == hand[0].suit for card in hand):
            print('Flush')
            self.tlist.append(6 * 13 ** 5 + self.point(hand))
        else:
            self.isStraight(hand)

    def isStraight(self, hand, flag: bool = True) -> None:
        # Printa 'Straight' se for verdadeiro, se não, passa para isThree(hand)
        Currank: int = hand[0].rank   
        for card in hand:
            if card.rank != Currank:
                flag: bool = False
                break
            else:
                Currank -= 1
        if flag:
            print('Straight')
            self.tlist.append(5 * 13 ** 5 + self.point(hand))
        else:
            self.isThree(hand)
            
    def isThree(self, hand) -> None:
        # Printa 'Three of a Kind' se for verdadeiro, se não, passa para isTwo(hand)
        # Em uma lista ordenada de 5 cartas, a carta do meio deve se repetir 3 vezes 
        if [card.rank for card in hand].count(hand[2].rank) == 3:
            print("Trinca")
            self.tlist.append(4 * 13 ** 5 + self.point(hand))
        else:
            self.isTwo(hand)
            
    def isTwo(self, hand) -> None:      
        # Printa 'Two Pair' se for verdadeiro, se não, passa para isPair(hand)
        # Em uma lista ordenada de 5 cartas, a segunda e a quarta carta devem se repetir
        if [card.rank for card in hand].count(hand[1].rank) == 2 and [card.rank for card in hand].count(hand[3].rank) == 2:
            print("Dois Pares")
            self.tlist.append(3 * 13 ** 5 + self.point(hand))
        else: 
            self.isOne(hand)
        
    def isOne(self, hand) -> None: 
        # Printa 'One Pair' se for verdadeiro, se não, passa para isHigh(hand)
        # Deve haver 2 cartas iguais e o restante deve ser diferente
        mycount: List[int] = list(map([card.rank for card in hand].count, [card.rank for card in hand]))
        if mycount.count(2) == 2 and mycount.count(1) == 3: 
            print("Par")
            self.tlist.append(2 * 13 ** 5 + self.point(hand))
        else:
            self.isHigh(hand)

    def isHigh(self, hand) -> None:         
        # Printa 'High Card' 
        print("Carta Mais Alta")
        self.tlist.append(13 ** 5 + self.point(hand))