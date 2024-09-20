import keyboard
import random
import time

def main():
    tabuleiro = [["0"] * 10 for _ in range(20)]
    pecas = [
        ["1", "1", "1", "1"], 
        [["1", "1"], ["1", "1"]], 
        [["1", "1", "1"], ["0", "1", "0"]], 
        [["0", "1", "1"], ["1", "1", "0"]], 
        [["1", "1", "0"], ["0", "1", "1"]], 
        [["1", "0", "0"], ["1", "1", "1"]], 
        [["0", "0", "1"], ["1", "1", "1"]]
        ]
    peca_aleatoria = random.choice(pecas)
    largura_peca = len(peca_aleatoria[0])
    coluna = random.randint(0, 9 - largura_peca)

    print_peca(peca_aleatoria, tabuleiro, coluna)

    for linha in tabuleiro:
        print(" ".join(linha))

def print_peca(peca_aleatoria, tabuleiro, coluna):
    for i in range(len(peca_aleatoria)):
        for j in range(len(peca_aleatoria[i])):
            if i < len(tabuleiro) and j + coluna < len(tabuleiro[0]):
                tabuleiro[i][j + coluna] = peca_aleatoria[i][j]

main()