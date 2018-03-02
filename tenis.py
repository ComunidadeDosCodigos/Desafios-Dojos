#Criado por:
#Caio Carnelos
#Kaio
#Diego

import os

def clear():
    os.system("cls")


estagio = [0, 15, 30, 40, 'deuce', 'vantagem', 'vitoria']

P1 = 0
P2 = 0 

while True:
    print("Player 1: {}".format(estagio[P1]))
    print("Player 2: {}".format(estagio[P2]))
    try:
        n = int(input('\n\t player: '))
    except ValueError:
        print("O Valor precisa ser inteiro!")

        n = int(input('\n\t player: '))
    clear()

    if n == 1:
        P1 += 1
    elif n == 2:
        P2 += 1

    if P1 == 3 and P2 == 3:
        P1 = 4
        P2 = 4

    #Aqui vai a regra da vantagem.
    if P1 == 5 and P2 == 5:
        P1 = 4
        P2 = 4

    if P1 >= 4 and P2 <= 2:
        print("\n\t Player 1 Venceu")
        break
    
    if P2 >= 4 and P1 <= 2:
        print("\n\t Player 2 Venceu")
        break

    if P1 == 6:
        print("\n\t Player 1 Venceu")
        break

    if P2 == 6:
        print("\n\t Player 2 Venceu")
        break     
