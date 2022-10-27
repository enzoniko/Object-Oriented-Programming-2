from dataclasses import dataclass, field
from typing import List
from deck import Deck
from card import Card

@ dataclass
class Poker(object):
    deck: Deck = field(default_factory=Deck)
    hands: List[Card] = field(default_factory=list)
    tlist: list = field(default_factory=list)
    num_hands: int = 0
    num_cards_in_hand: int = 5
    def __post_init__(self):
        self.deck.shuffle()
        for _ in range(self.num_hands):
            hand = [self.deck.deal() for _ in range (self.num_cards_in_hand)]
            self.hands.append(hand)
      
    def play(self):
        for i in range (len (self.hands) ):
            sortedHand = sorted (self.hands[i], reverse = True)
            hand = ''
            for card in sortedHand:
                hand = hand + str(card) + ' '
            print(f'Hand {str(i + 1)}: {hand}')

    def point(self,hand):                         #point()function to calculate partial score
        sortedHand=sorted(hand,reverse=True)
        c_sum=0
        ranklist = [card.rank for card in sortedHand]
        c_sum=ranklist[0]*13**4+ranklist[1]*13**3+ranklist[2]*13**2+ranklist[3]*13+ranklist[4]
        return c_sum

        
    def isRoyal (self, hand):               #returns the total_point and prints out 'Royal Flush' if true, if false, pass down to isStraightFlush(hand)
        sortedHand=sorted(hand,reverse=True)
        flag=True
        h=10
        Cursuit=sortedHand[0].suit
        Currank=14
        total_point=h*13**5+self.point(sortedHand)
        for card in sortedHand:
            if card.suit!=Cursuit or card.rank!=Currank:
                flag=False
                break
            else:
                Currank-=1
        if flag:
            print('Royal Flush')
            self.tlist.append(total_point)    
        else:
            self.isStraightFlush(sortedHand)
        

    def isStraightFlush (self, hand):       #returns the total_point and prints out 'Straight Flush' if true, if false, pass down to isFour(hand)
        sortedHand=sorted(hand,reverse=True)
        flag=True
        h=9
        Cursuit=sortedHand[0].suit
        Currank=sortedHand[0].rank
        total_point=h*13**5+self.point(sortedHand)
        for card in sortedHand:
            if card.suit!=Cursuit or card.rank!=Currank:
                flag=False
                break
            else:
                Currank-=1
        if flag:
            print ('Straight Flush')
            self.tlist.append(total_point)
        else:
            self.isFour(sortedHand)

    def isFour(self, hand):                  #returns the total_point and prints out 'Four of a Kind' if true, if false, pass down to isFull()
        sortedHand=sorted(hand,reverse=True)
        flag=True
        h=8
        Currank=sortedHand[1].rank               #since it has 4 identical ranks,the 2nd one in the sorted listmust be the identical rank
        total_point=h*13**5+self.point(sortedHand)
        count = sum(card.rank == Currank for card in sortedHand)
        if count >= 4:
            flag=True
            print('Four of a Kind')
            self.tlist.append(total_point)

        else:
            self.isFull(sortedHand)
        
    def isFull(self, hand):                     #returns the total_point and prints out 'Full House' if true, if false, pass down to isFlush()
        sortedHand=sorted(hand,reverse=True)
        flag=True
        h=7
        total_point=h*13**5+self.point(sortedHand)
        mylist = [card.rank for card in sortedHand]
        rank1=sortedHand[0].rank                  #The 1st rank and the last rank should be different in a sorted list
        rank2=sortedHand[-1].rank
        num_rank1=mylist.count(rank1)
        num_rank2=mylist.count(rank2)
        if (num_rank1==2 and num_rank2==3)or (num_rank1==3 and num_rank2==2):
            flag=True
            print ('Full House')
            self.tlist.append(total_point)

        else:
            flag=False
            self.isFlush(sortedHand)

    def isFlush(self, hand):                         #returns the total_point and prints out 'Flush' if true, if false, pass down to isStraight()
        sortedHand=sorted(hand,reverse=True)
        h=6
        total_point=h*13**5+self.point(sortedHand)
        Cursuit=sortedHand[0].suit
        flag = all(card.suit == Cursuit for card in sortedHand)
        if flag:
            print ('Flush')
            self.tlist.append(total_point)

        else:
            self.isStraight(sortedHand)

    def isStraight (self, hand):
        sortedHand=sorted(hand,reverse=True)
        flag=True
        h=5
        total_point=h*13**5+self.point(sortedHand)
        Currank=sortedHand[0].rank                        #this should be the highest rank
        for card in sortedHand:
            if card.rank!=Currank:
                flag=False
                break
            else:
                Currank-=1
        if flag:
            print('Straight')
            self.tlist.append(total_point)
        
        else:
            self.isThree(sortedHand)
            
    def isThree(self, hand):
        sortedHand=sorted(hand,reverse=True)
        flag=True
        h=4
        total_point=h*13**5+self.point(sortedHand)
        Currank=sortedHand[2].rank                    #In a sorted rank, the middle one should have 3 counts if flag=True
        mylist = [card.rank for card in sortedHand]
        if mylist.count(Currank)==3:
            flag=True
            print ("Three of a Kind")
            self.tlist.append(total_point)

        else:
            flag=False
            self.isTwo(sortedHand)
            
    def isTwo(self, hand):                           #returns the total_point and prints out 'Two Pair' if true, if false, pass down to isOne()
        sortedHand=sorted(hand,reverse=True)
        flag=True
        h=3
        total_point=h*13**5+self.point(sortedHand)
        rank1=sortedHand[1].rank                        #in a five cards sorted group, if isTwo(), the 2nd and 4th card should have another identical rank
        rank2=sortedHand[3].rank
        mylist = [card.rank for card in sortedHand]
        if mylist.count(rank1)==2 and mylist.count(rank2)==2:
            flag=True
            print ("Two Pair")
            self.tlist.append(total_point)

        else:
            flag=False
            self.isOne(sortedHand)
        
    def isOne(self, hand):                            #returns the total_point and prints out 'One Pair' if true, if false, pass down to isHigh()
        sortedHand=sorted(hand,reverse=True)
        flag=True
        h=2
        total_point=h*13**5+self.point(sortedHand)
        mycount=[]                                      #create an empty list to store number of count of each rank
        mylist = [card.rank for card in sortedHand]
        for each in mylist:
            count=mylist.count(each)
            mycount.append(count)
        if mycount.count(2)==2 and mycount.count(1)==3:  #There should be only 2 identical numbers and the rest are all different
            flag=True
            print ("One Pair")
            self.tlist.append(total_point)

        else:
            flag=False
            self.isHigh(sortedHand)

    def isHigh(self, hand):                          #returns the total_point and prints out 'High Card' 
        sortedHand=sorted(hand,reverse=True)
        flag=True
        h=1
        total_point=h*13**5+self.point(sortedHand)
        mylist = [card.rank for card in sortedHand]
        print ("High Card")
        self.tlist.append(total_point)