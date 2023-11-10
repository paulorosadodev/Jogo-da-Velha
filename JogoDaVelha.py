import os
os.system('cls')

matriz = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

def printarMatriz(matriz):
    for i in range(3):
        for j in range(3):
            print(f"{matriz[i][j]}", end = " ")
        print()

def registrarJogada(jogada):
    for i in range(3):
        for j in range(3):
            if jogada == jogadaX:
                if int(jogadaX[0]) == i+1 and int(jogadaX[1]) == j+1:
                    matriz[i][j] = 'X'
            elif jogada == jogadaO:
                if int(jogadaO[0]) == i+1 and int(jogadaO[1]) == j+1:
                    matriz[i][j] = 'O'

def analiseColuna(coluna, jogada):
    colunas = []
    for i in range(3):
        colunas.append(matriz[i][coluna])
    if colunas.count(jogada) == 3:
        print()
        print(f'{jogada} venceu!')
        return 'end'


def analisarJogo(matriz, jogada):
    for i in range(3):
        for j in range(3):
            if jogada == jogadaX: 
                if analiseColuna(j, 'X') == 'end':
                    return 'end'
                elif matriz[i].count('X') == 3: #Linha
                    print()
                    print(f"X venceu!")
                    return 'end' 

            
            elif jogada == jogadaO:
                if matriz[i].count('O') == 3:
                    print()
                    print(f"O venceu!")
                    return 'end'

rodada = 0

while True:
    if rodada > 0:
        print()
    jogadaX = input("Digite respectivamente a linha (l) e a coluna (c) em que deseja jogar 'X' no formato [lc]: ").upper()
    print()
    registrarJogada(jogadaX)
    printarMatriz(matriz)
    rodada += 1

    if rodada >= 5:
        if analisarJogo(matriz, jogadaX) == 'end':
            break

    
    print()
    jogadaO = input("Digite respectivamente a linha (l) e a coluna (c) em que deseja jogar 'O' no formato [lc]: ").upper()
    print()
    registrarJogada(jogadaO)
    printarMatriz(matriz)
    rodada += 1

    if rodada >= 5:
        if analisarJogo(matriz, jogadaO) == 'end':
            break