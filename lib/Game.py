class Game():
    def boatPlacementChoice(self, matrizJogada, linha, coluna, matrizTabuleiro, isPlayer):
        while True:
            if matrizJogada[linha-1][coluna-1] != 0:
                print('Posição já ocupada')
                linha = int(input('Digite a linha: '))
                coluna = int(input('Digite a coluna: '))
            else:
                matrizJogada[linha-1][coluna-1] = 1
                if isPlayer:
                    matrizTabuleiro[linha-1][coluna-1] = '\033[94mO\033[0m'
                break
    
    def jogada(self, matrizJogada, matrizTabuleiro,linha,coluna):    
        matrizTabuleiro[linha-1][coluna-1] = 1
        
        if matrizJogada[linha-1][coluna-1] == matrizTabuleiro[linha-1][coluna-1]:
            matrizTabuleiro[linha-1][coluna-1] = '\033[92mX\033[0m'
            print('\033[92mNavio inimigo atingido!\033[0m')
        else:
            matrizTabuleiro[linha-1][coluna-1] = '\033[91mO\033[0m'
            print('\033[91mNenhum navio atingido!\033[0m')