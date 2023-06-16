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
    counter = 0
    counterp = 0
    counterc = 0
    isIntro = True
    text.welcome()
    while True:
        text.clear()
        if isIntro:
            while counter < 5:
                text.intro(counter)
                try:
                    linha = int(input('Digite a linha: '))
                    coluna = int(input('Digite a coluna: '))
                    
                    game.boatPlacementChoice(matrizes.player, linha, coluna, matrizes.playerTela, True)
                    game.boatPlacementChoice(matrizes.computador, random.randint(0, 4), random.randint(0, 9), matrizes.playerTela, False)
                    text.clear()
                    counter += 1
                except Exception:
                    text.clear()
                    print("Caractere Inválido!")
                    continue
        isIntro = False
        for i in range(5):
            for j in range(10):
                if matrizes.playerTela[i][j] == '\033[92mX\033[0m':
                    counterc += 1
                elif matrizes.computadorTela[i][j] == '\033[92mX\033[0m':
                    counterp += 1  
            
        if counterp == 5:
            text.clear()
            text.endGame('player')
            break
        elif counterc == 5:
            text.clear()
            text.endGame('computador')
            break
        counterc = 0
        counterp = 0
        text.tabuleiro(matrizes.playerTela, matrizes.computadorTela)
        time.sleep(1)
        text.ataque()
        while True:
            try:
                linha = int(input('Digite a linha: '))
                coluna = int(input('Digite a coluna: '))
                text.clear()
            
                game.jogada(matrizes.computador, matrizes.computadorTela, linha, coluna)
                text.tabuleiro(matrizes.playerTela, matrizes.computadorTela)
                break
            except Exception:
                    text.clear()
                    text.tabuleiro(matrizes.playerTela, matrizes.computadorTela)
                    print("Caractere Inválido!")
                    continue
        time.sleep(1)
        text.ataqueIA()
        time.sleep(1)
        text.clear()
        
        game.jogada(matrizes.player, matrizes.playerTela, random.randint(0, 4), random.randint(0, 9))
        text.tabuleiro(matrizes.playerTela, matrizes.computadorTela)
        time.sleep(1)
        
        
if __name__ == "__main__":
    main()