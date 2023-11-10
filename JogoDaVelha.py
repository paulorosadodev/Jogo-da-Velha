import os
os.system('cls')

matriz = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

def registrarJogada(jogada, matriz):
    try:
        for i in range(3):
            for j in range(3):
                if jogada == jogadaX:
                    if int(jogadaX[0]) == i+1 and int(jogadaX[1]) == j+1:
                        if matriz[i][j] == '.':
                            matriz[i][j] = 'X'
                            return True
                    else: 
                        print('JOGADA INVÁLIDA')
                        print()
                        return False
                elif jogada == jogadaO:
                    if int(jogadaO[0]) == i+1 and int(jogadaO[1]) == j+1:
                        if matriz[i][j] == '.':
                            matriz[i][j] = 'O'
                            return True
                    else: 
                        print('JOGADA INVÁLIDA')
                        print()
                        return False
    except:
        print('DIGITE UM VALOR VÁLIDO')
        print()
        return False

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
    

def analiseDiagonal2(matriz, jogada):
    diagonal = []
    diagonal.append(matriz[2][0])
    diagonal.append(matriz[1][1])
    diagonal.append(matriz[0][2])
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
                elif analiseDiagonal2(matriz, 'X') == True:
                    return True
                else:
                    return False
            elif jogada == jogadaO:
                if analiseColuna(j, 'O') == True:
                    return True
                elif analiseLinha(i, 'O') == True: 
                    return True
                elif analiseDiagonal1(matriz, 'O') == True:
                    return True
                elif analiseDiagonal2(matriz, 'O') == True:
                    return True
                else:
                    return False

rodada = 0
começou = 0

while True:
    if começou == 0:
        print()
    
    jogadaX = input("Digite respectivamente a linha (l) e a coluna (c) em que deseja jogar 'X' no formato [lc]: ").upper()
    print()
    if registrarJogada(jogadaX, matriz) == True:
        printarMatriz(matriz)
        print()
        rodada += 1
    começou += 1

    if rodada >= 5:
        if analisarJogo(matriz, jogadaX) == True:
            break
    if rodada == 9 and analisarJogo(matriz, jogadaX) == False:
        print()
        print('Empate!')
        break

    jogadaO = input("Digite respectivamente a linha (l) e a coluna (c) em que deseja jogar 'O' no formato [lc]: ").upper()
    print()
    if registrarJogada(jogadaO, matriz) == True:
        printarMatriz(matriz)
        rodada += 1
    começou += 1

    if rodada >= 5:
        if analisarJogo(matriz, jogadaO) == True:
            break
