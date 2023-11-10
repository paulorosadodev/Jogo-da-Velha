import os
os.system('cls')

matriz = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

def registrarJogada(jogada):
    for i in range(3):
        for j in range(3):
            if jogada == jogadaX:
                if int(jogadaX[0]) == i+1 and int(jogadaX[1]) == j+1:
                    matriz[i][j] = 'X'
            elif jogada == jogadaO:
                if int(jogadaO[0]) == i+1 and int(jogadaO[1]) == j+1:
                    matriz[i][j] = 'O'

def printarMatriz(matriz):
    for i in range(3):
        for j in range(3):
            print(f"{matriz[i][j]}", end = " ")
        print()

def analiseLinha(linha, jogada):
    if matriz[linha].count(jogada) == 3:
        print()
        print(f"{jogada} venceu!")
        return True

def analiseColuna(coluna, jogada):
    colunas = []
    for i in range(3):
        colunas.append(matriz[i][coluna])
    if colunas.count(jogada) == 3:
        print()
        print(f'{jogada} venceu!')
        return True

def analiseDiagonal1(matriz, jogada):
    diagonal = []
    for i in range(3):
        for j in range(3):
            if i == j:
                diagonal.append(matriz[i][j])
    if diagonal.count(jogada) == 3:
        print()
        print(f'{jogada} venceu!')
        return True


def analisarJogo(matriz, jogada):
    for i in range(3):
        for j in range(3):
            if jogada == jogadaX: 
                if analiseColuna(j, 'X') == True:
                    return True
                elif analiseLinha(i, 'X') == True: 
                    return True
                elif analiseDiagonal1(matriz, 'X') == True:
                    return True
            elif jogada == jogadaO:
                if analiseColuna(j, 'O') == True:
                    return True
                elif analiseLinha(i, 'O') == True: 
                    return True
                elif analiseDiagonal1(matriz, 'O') == True:
                    return True

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
        if analisarJogo(matriz, jogadaX) == True:
            break

    print()
    
    jogadaO = input("Digite respectivamente a linha (l) e a coluna (c) em que deseja jogar 'O' no formato [lc]: ").upper()
    print()
    registrarJogada(jogadaO)
    printarMatriz(matriz)
    
    rodada += 1

    if rodada >= 5:
        if analisarJogo(matriz, jogadaO) == True:
            break