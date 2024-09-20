import keyboard
import random
import time

def main():
    # Declaração do tabuleiro, 10 colunas e 20 linhas
    tabuleiro = [["0"] * 10 for _ in range(20)]
    # Declaração das peças dentro de uma matriz, para peças com 2 colunas foram usadas matrizes dentro da matriz
    pecas = [
        ["1", "1", "1", "1"], 
        [["1", "1"], ["1", "1"]], 
        [["1", "1", "1"], ["0", "1", "0"]], 
        [["0", "1", "1"], ["1", "1", "0"]], 
        [["1", "1", "0"], ["0", "1", "1"]], 
        [["1", "0", "0"], ["1", "1", "1"]], 
        [["0", "0", "1"], ["1", "1", "1"]]
        ]
    # Declaração de peças aleatória, utiliza choice para determinar um item aleatória da lista peças
    peca_aleatoria = random.choice(pecas)
    # Determina a largura da peça aleatória selecionada
    largura_peca = len(peca_aleatoria[0])
    # Determina a coluna em que a peça vai cair, utiliza randint para selecionar um inteiro aleatória de 0 até 9 - a largura da peça
    # A razão para verificar a largura da peça é garantir que a peça não extrapole os limites do tabuleiro
    coluna = random.randint(0, 9 - largura_peca)

    # Chama a função "print_peça"
    print_peca(peca_aleatoria, tabuleiro, coluna)

    # Exibição do tabuleiro, identa em cada linha da lista, utilizando de join para unir os valores da linha com um espaço entre eles
    for linha in tabuleiro:
        print(" ".join(linha))

'''
Função print_peça:
Um loop que identa pelas colunas, dentro de um loop que identa pelas linhas da peça
Substitui o [i][j+coluna] (linha e coluna) do tabuleiro pelo [i][j] (linha e coluna) da peça
'''
def print_peca(peca_aleatoria, tabuleiro, coluna):
    for i in range(len(peca_aleatoria)):
        for j in range(len(peca_aleatoria[i])):
            tabuleiro[i][j + coluna] = peca_aleatoria[i][j]

main()