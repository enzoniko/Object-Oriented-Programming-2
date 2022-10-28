from time import sleep
from poker import Poker

def main(num_jogadores: int = 6):
  # Se quiser pedir pro usuário digitar o número de jogadores, descomente as linhas abaixo
  # Pede pro usuário digitar o número de jogadores
  # num_jogadores: int = int(input('Digite o número de jogadores: '))
  # while (num_jogadores < 2 or num_jogadores > 6):
  #   num_jogadores: int = int(input('Digite o número de jogadores: '))

  # Se quiser demorar um tempo respectivo ao número de jogadores, coloque num_jogadores/2 nos sleep
  # Cria o objeto Poker
  print("...Distribuindo as cartas...")
  game: Poker = Poker(num_hands = num_jogadores)
  sleep(1)
  print('--------------------------------------------------------------')
  # Distribui as cartas pra cada jogador
  game.play()
  print("...Calculando os pontos...")
  sleep(1)
  print('\n')

  # Mostra o tipo da mão de cada jogador
  for num_jogador, mao_atual in enumerate(game.hands):
    print(f"Jogador {str(num_jogador + 1)}: ", end="")
    game.isRoyal(mao_atual)

  # Mostra o vencedor
  print('\nJogador %d venceu'% (game.tlist.index(max(game.tlist)) + 1))
  
if __name__ == "__main__":
  # Roda o programa
  # Se quiser deixar o usuário digitar se deseja simular novamente, descomente as linhas abaixo
  # Se quiser controlar a quantidade de jogadores, bote o número de jogadores como argumento da função main()
  while True:
      main(10)
      # if input('Deseja simular novamente? (s/n)') == 'n':
      #     break
      