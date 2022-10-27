from time import sleep
from poker import Poker


def main():
  numHands = eval (input ('Enter number of hands to play: '))
  while (numHands < 2 or numHands > 6):
    numHands = eval( input ('Enter number of hands to play: ') )

  print("...Dealing cards...")
  game = Poker(num_hands=numHands)
  sleep(2)
  game.play()
  print("...Calculating scores...")
  sleep(2)

  print('\n')
  for i in range(numHands):
    curHand=game.hands[i]
    print(f"Hand {str(i + 1)}: ", end="")
    game.isRoyal(curHand)

  maxpoint=max(game.tlist)
  maxindex=game.tlist.index(maxpoint)

  print ('\nHand %d wins'% (maxindex+1))
  
if __name__ == "__main__":
    while True:
        main()
        if input("Play again? (y/n): ") != "y":
            break
  