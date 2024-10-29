'''
Objetivo da função:
Fazer a peça girar

Como essa função funciona:
A matriz é invertida, pra que o giro possa ser visualmente no sentido horario, porque somente o zip na matriz iriaa fazer girar no anti-horario
Os elementos de cada indice da matriz são agrupados pela função zip, basicamente as colunas se tornam linhas
É retornado uma nova lista(matriz), com cada uma das novas listas geradas pelo zip
'''
def girar_peca(peca_aleatoria):
    return [list(linha) for linha in zip(*peca_aleatoria[::-1])]

'''
Objetivo da função:
Print peça no tabuleiro na posição atual
Como essa função funciona:
Itera pelas linhas e colunas da peça e printa na posição do tabuleiro que é indicada pelas variaveis de linha e coluna
que são alteradas no funcionamento do código principal
'''
def print_peca(peca_aleatoria, tabuleiro, coluna, linha):
    for x in range(len(peca_aleatoria)):
        for y in range(len(peca_aleatoria[x])):
            if peca_aleatoria[x][y] in ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫", "💣"]:
                tabuleiro[linha + x][coluna + y] = peca_aleatoria[x][y]

'''
Objetivo da função:
apagar a peça da posição antiga
Como essa função funciona:
Troca onde estava a peça anteriormente por blocos vazios que representam o tabuleiro
Basicamente no main ele apaga peça, adiciona linha, printa peça, o que da a impressão de quedas
'''
def apagar_peca(peca_aleatoria, tabuleiro, coluna, linha):
    for x in range(len(peca_aleatoria)):
        for y in range(len(peca_aleatoria[x])):
            if peca_aleatoria[x][y] in ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫", "💣"]:
                tabuleiro[linha + x][coluna + y] = "⬛"

'''
Objetivo da função:
Verificar se a peça pode se mover (cair, esquerda, direita e giro)
Como essa função funciona:
Itera pelas linhas e colunas da peça, verifica se o elemento é peça e não vazio
Verifica então as condições:
1. Se a linha abaixo supera o limite do tabuleiro
2. Se pra esquerda ou para a direita vai passar dos limites do tabuleiro
3. Se vai colidir com uma peça já existente no tabuleiro
Se qualquer uma das condições for real, retorna true e detecta colisão
Se nenhuma for real, retorna false ou seja sem colisão
'''
def colidir(peca_aleatoria, tabuleiro, coluna, linha_abaixo):
    for x in range(len(peca_aleatoria)):
        for y in range(len(peca_aleatoria[x])):
            if peca_aleatoria[x][y] in ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫", "💣"]:
                if linha_abaixo + x >= len(tabuleiro) - 1 or coluna + y < 1 or coluna + y >= len(tabuleiro[0]) - 1 or tabuleiro[linha_abaixo + x][coluna + y] != "⬛":
                    return True
    return False

'''
Objetivo da função:
Printar o tabuleiro na tela
Como essa função funciona:
Itera por cada linha do tabuleiro, printando cada um dos elementos
A utilização de join é para que printe individualmente cada elemento parecendo um tabuleiro e não em forma de listas
'''
def printar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("".join(linha))

'''
Objetivo da função:
Verificar se alguma linha foi completa e dar pontuaçao com base nas linhas completas
Como essa função funciona:
A função inicia uma lista vazia para armazenar os indices das linhas completas. Depois um loop itera por todas as linhas do tabuleiro (exceto a ultima) verificando
se do indice 1 até o indice 10 tem algum bloco preto (que repesenta o tabuleiro), caso não tenha nenhum então o indice dessa linha é armazenado na lista inicial. 
Após verificar todas as linhas é iniciado outro loop que itera pelos indices recebidos, e então deleta as linhas que foram totalmente preenchidas e 
adiciona uma nova linha sem blocos no inicio do tabuleiro. Então a função retorna o "len" de linhas_removidas, ou seja, a quantidade de linhas que foram removidas.
'''

def linha_completa(tabuleiro):
    linhas_removidas = []
    for x in range(len(tabuleiro) - 1):
        linha = tabuleiro[x][1:-1]
        if "⬛" not in linha and "💣" not in linha:
            linhas_removidas.append(x)

    for x in linhas_removidas:
        del tabuleiro[x]
        tabuleiro.insert(0, ["⬜"] + ["⬛"] * 10 + ["⬜"])

    return len(linhas_removidas)


'''
Essa função é somente para printar o menu inicial
'''
def menu_inicial(largura_terminal):
    print(r''' .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |  _________   | || |  _________   | || |  _______     | || |     _____    | || |    _______   | |
| | |  _   _  |  | || | |_   ___  |  | || | |  _   _  |  | || | |_   __ \    | || |    |_   _|   | || |   /  ___  |  | |
| | |_/ | | \_|  | || |   | |_  \_|  | || | |_/ | | \_|  | || |   | |__) |   | || |      | |     | || |  |  (__ \_|  | |
| |     | |      | || |   |  _|  _   | || |     | |      | || |   |  __ /    | || |      | |     | || |   '.___`-.   | |
| |    _| |_     | || |  _| |___/ |  | || |    _| |_     | || |  _| |  \ \_  | || |     _| |_    | || |  |`\____) |  | |
| |   |_____|    | || | |_________|  | || |   |_____|    | || | |____| |___| | || |    |_____|   | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
'----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
''')

    print("1. Jogar".center(largura_terminal))
    print("2. Regras".center(largura_terminal))
    print("3. Sair".center(largura_terminal))

'''
Objetivo da função:
Verificar se o critério de derrota foi atendido
Como essa função funciona:
Assim como no JOGO ORIGINAL do Tetris, caso QUALQUER bloco esteja fixado na primeira linha, o jogo acaba, independene se há espaço para outras peças ou não.
Nesse caso é verificado se há qualquer bloco na linha extra que foi criada, a linha 21 (que está no index 0), caso exista qualquer bloco nessa linha então é retornado True
na função.
'''
def game_over(tabuleiro):
    blocos = ["🟫", "🟪", "🟦", "🟩", "🟨", "🟧", "🟥"]
    return any(bloco in blocos for bloco in tabuleiro[0])

'''
Essa função é somente para printar as regras
'''
def print_regras():
    print("1. O tabuleiro possui 10 colunas e 21 linhas, porém apenas 20 linhas podem estar ocupadas com blocos.")
    print("2. Existem 8 tipos de peças, peças aleatórias aparecem no topo do tabuleiro em uma coluna aleatória e com rotações diferentes.")
    print("3. Uma das peças é a \"bomba\", quando essa peça encontra colisão e para, ela destroi os blocos que estão no seu raio ao redor.")
    print("4. Quando uma linha é completamente preenchida com blocos, ela é removida do tabuleiro.")
    print("4. Ao remover uma linhas, todas que estavam acima descem.")
    print("5. O jogador ganha pontos por linhas removidas, caso sejam removidas 2, 3 ou 4 linhas simultâneas, a pontuação é dobrada para cada linha.")
    print("6. O jogo termina se algum bloco sair do limite aceito, ou seja, se na primeira linha houver algum bloco.")
    print("7. Os controles do jogo são: W para girar, A para esquerda, D para direita e S para cair mais rápido.")
    input("\nAPERTE ENTER PARA VOLTAR AO MENU INICIAL.")

'''
Objetivo da função:
Verificar se há uma bomba no tabuleiro, se tiver, limpar a área 3x3 ao redor dela
Como essa função funciona:
Primeiramenta a função entra no loop, onde verifica todos os elementos do tabuleiro, se algum deles for uma bomba, então armazena a linha e a coluna que a bomba está
Após isso, com base na linha e coluna armazenadas, os elementos ao redor são trocados pelos quadrados pretos que representam o tabuleiro
Os elementos só são trocados pelos quadrados pretos se passarem nas validações, que foram feitas para que as bordas do tabuleiro não sejam apagadas
'''
def peca_bomba(tabuleiro):
    for x in range(len(tabuleiro)-1):
        for y in range(len(tabuleiro[x])):
            if tabuleiro[x][y] == "💣":
                linha = x
                coluna = y

    if linha+1 != 21:
        tabuleiro[linha+1][coluna] = "⬛"
        if coluna-1 != 0:
            tabuleiro[linha+1][coluna-1] = "⬛"
        if coluna+1 != 11:
            tabuleiro[linha+1][coluna+1] = "⬛"
    if linha-1 != -1:
        tabuleiro[linha-1][coluna] = "⬛"
        if coluna-1 != 0:
            tabuleiro[linha-1][coluna-1] = "⬛"
        if coluna+1 != 11:
            tabuleiro[linha-1][coluna+1] = "⬛"
    if coluna-1 != 0:
        tabuleiro[linha][coluna-1] = "⬛"
    if coluna+1 != 11:
        tabuleiro[linha][coluna+1] = "⬛"
    tabuleiro[linha][coluna] = "⬛"