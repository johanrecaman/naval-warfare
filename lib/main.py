import random
import time
from Game import Game
from Matrizes import Matrizes
from Text import Text

text = Text
matrizes = Matrizes()
game = Game()

linha = 0
coluna = 0

def main():
    isIntro = True
    while True:
        text.clear()
        if isIntro:
            for i in range(5):
                text.intro(i)
                linha = int(input('Digite a linha: '))
                coluna = int(input('Digite a coluna: '))
                game.boatPlacementChoice(matrizes.player, linha, coluna)
                game.boatPlacementChoice(matrizes.computador, random.randint(0, 4), random.randint(0, 9))
                text.clear()
        isIntro = False
        text.tabuleiro(matrizes.playerTela, matrizes.computadorTela)
        text.ataque()
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        text.clear()
        
        game.jogada(matrizes.computador, matrizes.computadorTela, linha, coluna)
        text.tabuleiro(matrizes.playerTela, matrizes.computadorTela)
        
        time.sleep(1)
        text.ataqueIA()
        time.sleep(1)
        text.clear()
        
        game.jogada(matrizes.player, matrizes.playerTela, random.randint(0, 4), random.randint(0, 9))
        text.tabuleiro(matrizes.playerTela, matrizes.computadorTela)
        time.sleep(1)
        
        if matrizes.playerTela.count('X') == 5:
            text.endGame('Computador')
            break
        elif matrizes.computadorTela.count('X') == 5:
            text.endGame('Jogador')
            break
        
if __name__ == "__main__":
    main()