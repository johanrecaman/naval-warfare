import os
class Text():
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def intro(i):
        print(f"Bem vindo ao jogo Batalha Naval! \n Digite a posição inicial de seu {i+1}º navio:")
    
    def ataque():
        print("Digite a posição que deseja atacar:")
    
    def ataqueIA():
        print("A IA está atacando...")
        
    def tabuleiro(x, y):
        print(f''' Tabuleiro do Jogador:                         Tabuleiro computador:  
  {x[0][0]} | {x[0][1]} | {x[0][2]} | {x[0][3]} | {x[0][4]} | {x[0][5]} | {x[0][6]} | {x[0][7]} | {x[0][8]} | {x[0][9]}         {y[0][0]} | {y[0][1]} | {y[0][2]} | {y[0][3]} | {y[0][4]} | {y[0][5]} | {y[0][6]} | {y[0][7]} | {y[0][8]} | {y[0][9]}       
-----------------------------------------     -----------------------------------------  
  {x[1][0]} | {x[1][1]} | {x[1][2]} | {x[1][3]} | {x[1][4]} | {x[1][5]} | {x[1][6]} | {x[1][7]} | {x[1][8]} | {x[1][9]}         {y[1][0]} | {y[1][1]} | {y[1][2]} | {y[1][3]} | {y[1][4]} | {y[1][5]} | {y[1][6]} | {y[1][7]} | {y[1][8]} | {y[1][9]}   
-----------------------------------------     -----------------------------------------      
  {x[2][0]} | {x[2][1]} | {x[2][2]} | {x[2][3]} | {x[2][4]} | {x[2][5]} | {x[2][6]} | {x[2][7]} | {x[2][8]} | {x[2][9]}         {y[2][0]} | {y[2][1]} | {y[2][2]} | {y[2][3]} | {y[2][4]} | {y[2][5]} | {y[2][6]} | {y[2][7]} | {y[2][8]} | {y[2][9]}       
-----------------------------------------     -----------------------------------------                                              
  {x[3][0]} | {x[3][1]} | {x[3][2]} | {x[3][3]} | {x[3][4]} | {x[3][5]} | {x[3][6]} | {x[3][7]} | {x[3][8]} | {x[3][9]}         {y[3][0]} | {y[3][1]} | {y[3][2]} | {y[3][3]} | {y[3][4]} | {y[3][5]} | {y[3][6]} | {y[3][7]} | {y[3][8]} | {y[3][9]}       
-----------------------------------------     -----------------------------------------                                                   
  {x[4][0]} | {x[4][1]} | {x[4][2]} | {x[4][3]} | {x[4][4]} | {x[4][5]} | {x[4][6]} | {x[4][7]} | {x[4][8]} | {x[4][9]}         {y[4][0]} | {y[4][1]} | {y[4][2]} | {y[4][3]} | {y[4][4]} | {y[4][5]} | {y[4][6]} | {y[4][7]} | {y[4][8]} | {y[4][9]} 
''')
    
    def erro():
        print("Posição inválida, digite novamente:")
        
    def endGame(x):
        print(f'''Vitoria do {x}!
        Feito por:
        Felipe Augusto
        Johan Stromberg
        Evandro Diniz
        Giuseppe Bruno
        André Eller''')