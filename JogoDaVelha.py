import os
os.system('cls')

matriz = [['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️']]

def registrarJogada(jogada):
    for i in range(3):
        for j in range(3):
            if jogada == jogadaX:
                if int(jogadaX[0]) == i+1 and int(jogadaX[1]) == j+1:
                    if matriz[i][j] == '⬜️':
                        matriz[i][j] = '❌'
                        return True
            elif jogada == jogadaO:
                if int(jogadaO[0]) == i+1 and int(jogadaO[1]) == j+1:
                    if matriz[i][j] == '⬜️':
                        matriz[i][j] = '⭕️'
                        return True

def printarMatriz(matriz):
    for i in range(3):
        for j in range(3):
            print(f"{matriz[i][j]}", end = "")
        print()

def analiseLinha(linha, jogada):
    if matriz[linha].count(jogada) == 3:
        print('🎉🎉🎉🎉🎉')
        print(f"{jogada} venceu!")
        return True

def analiseColuna(coluna, jogada):
    colunas = []
    for i in range(3):
        colunas.append(matriz[i][coluna])
    if colunas.count(jogada) == 3:
        print('🎉🎉🎉🎉🎉')
        print(f'{jogada} venceu!')
        return True


def analiseDiagonal1(matriz, jogada):
    diagonal = []
    for i in range(3):
        for j in range(3):
            if i == j:
                diagonal.append(matriz[i][j])
    if diagonal.count(jogada) == 3:
        print('🎉🎉🎉🎉🎉')
        print(f'{jogada} venceu!')
        return True
    

def analiseDiagonal2(matriz, jogada):
    diagonal = []
    diagonal.append(matriz[2][0])
    diagonal.append(matriz[1][1])
    diagonal.append(matriz[0][2])
    if diagonal.count(jogada) == 3:
        print()
        print('🎉🎉🎉🎉🎉')
        print()
        print(f'{jogada} venceu!')
        return True

def analisarJogo(matriz, jogada):
    for i in range(3):
        for j in range(3):
            if jogada == jogadaX: 
                if analiseColuna(j, '❌') == True:
                    return True
                elif analiseLinha(i, '❌') == True: 
                    return True
                elif analiseDiagonal1(matriz, '❌') == True:
                    return True
                elif analiseDiagonal2(matriz, '❌') == True:
                    return True
            elif jogada == jogadaO:
                if analiseColuna(j, '⭕️') == True:
                    return True
                elif analiseLinha(i, '⭕️') == True: 
                    return True
                elif analiseDiagonal1(matriz, '⭕️') == True:
                    return True
                elif analiseDiagonal2(matriz, '⭕️') == True:
                    return True


rodada = 0

while True:
    if rodada == 0:
        print()
    
    while True:
        try:
            jogadaX = input("Digite respectivamente a linha (l) e a coluna (c) em que deseja jogar '❌' no formato [lc]: ")
            print()
            if registrarJogada(jogadaX) == True:
                printarMatriz(matriz)
                print()
                rodada += 1
                break
            else:
                print('⚠️  JOGADA INVÁLIDA')
                print()
        except:
            print('⚠️  JOGADA INVÁLIDA')
            print()

    if rodada >= 5:
        if analisarJogo(matriz, jogadaX) == True:
            break
    if rodada == 9 and analisarJogo(matriz, jogadaX) != True:
        print('Empate!')
        break

    while True:
        try:
            jogadaO = input("Digite respectivamente a linha (l) e a coluna (c) em que deseja jogar '⭕️' no formato [lc]: ")
            print()
            if registrarJogada(jogadaO) == True:
                printarMatriz(matriz)
                print()
                rodada += 1
                break
            else:
                print('⚠️  JOGADA INVÁLIDA')
                print()
        except:
            print('⚠️  JOGADA INVÁLIDA')
            print()

    if rodada >= 5:
        if analisarJogo(matriz, jogadaO) == True:
            break