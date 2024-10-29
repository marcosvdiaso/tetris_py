import random, time, os, keyboard
from tetris import *

def main():
    fechar = False

    # Enquanto a variável fechar for False, o programa continua rodando em loop
    while not fechar:
        # O tabuleiro possui uma linha a mais para que caso qualquer bloco fique na linha 21 (index 0), seja dado game over
        tabuleiro = [["⬜"] + ["⬛"] * 10 + ["⬜"] for _ in range(21)] + [["⬜"] * 12]
        pont = 0
        tempo_queda = 0.5
        metade_tempo_queda = tempo_queda / 2
        largura_terminal = os.get_terminal_size().columns # Variável para obter a largura do terminal, utilizada em menu inicial
        fim = False

        i = [["🟧"], ["🟧"], ["🟧"], ["🟧"]]
        q = [["🟨", "🟨"], ["🟨", "🟨"]]
        t = [["🟩", "🟩", "🟩"], ["⬛", "🟩", "⬛"]]
        s = [["⬛", "🟦", "🟦"], ["🟦", "🟦", "⬛"]]
        z = [["🟪", "🟪", "⬛"], ["⬛", "🟪", "🟪"]]
        l = [["🟫", "⬛", "⬛"], ["🟫", "🟫", "🟫"]]
        j = [["⬛", "⬛", "🟥"], ["🟥", "🟥", "🟥"]]
        bomba = [["💣"]]
        pecas = [i, q, t, s, z, l, j]

        '''
        Menu inicial do programa, há uma verificação que verifica se o valor digitado é um inteiro e se está entre 1 e 3
        Se o valor for inválido a escolha fica rodando em loop 
        '''
        menu_inicial(largura_terminal)
        escolha = input("\n".center(largura_terminal))
        while not escolha.isdigit() or int(escolha) not in range(1, 4):
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_inicial(largura_terminal)
            escolha = input("\n".center(largura_terminal))
        escolha = int(escolha)

        # Dependendo da escolha, entra em uma parte diferente do programa
        match escolha:
            case 1:
                linha = 0
                peca_aleatoria = random.choice(pecas) # É escolhida uma peça inicial aleatória
                # Sorteio para decidir se a peça irá aparecer em sua posição normal ou rotacionada
                if random.choice([True, False]):
                    for x in range(random.randint(1, 3)): # Caso vá ser rotacionada, sorteia de 1 a 3 para que ela possa vir em qualquer uma das 3 rotações possíveis
                        peca_aleatoria = girar_peca(peca_aleatoria)
                coluna = random.randint(1, 10 - len(peca_aleatoria[0])) # Sorteia a coluna em que vai aparecer
                pecas.append(bomba) # Adiciona bomba depois na lista de pecas, pra que ela não seja a primeira peça a aparecer, quando o tabuleiro está vazio

                os.system('cls' if os.name == 'nt' else 'clear')
                print("3")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')

                
                print("3...2")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')

                print("3...2...1!")
                time.sleep(1)
                time.sleep(0.1)

                '''
                Enquanto a variável fim for False o jogo roda
                O loop do programa basicamente é: Apagar peça de posição anterior, verificar se há linha completa e pontuação,
                verificar se há colisão, se tiver, printar nova peça, se não tiver, continuar printando a peça atual caindo
                Todas as funções estão explicadas em tetris.py
                '''
                while not fim:
                    apagar_peca(peca_aleatoria, tabuleiro, coluna, linha)
                    linhas_removidas = linha_completa(tabuleiro) # Atribui o numero de linhas completas para linhas removidas
                    # Se linhas removidas for maior que 0 faz o calculo da pontuação que é exponencial com base no número de multiplas linhas removidas
                    if linhas_removidas > 0:
                        pont += 100 * (2 ** (linhas_removidas - 1))

                    # Se for apertado A, é removido 1 da coluna, ou seja, vai para a esquerda, se não tiver colisão
                    if keyboard.is_pressed('a'):
                        if not colidir(peca_aleatoria, tabuleiro, coluna - 1, linha):
                            coluna -= 1

                    # Se for apertado D, é adicionado 1 da coluna, ou seja, vai para a direita, se não tiver colisão
                    if keyboard.is_pressed('d'):
                        if not colidir(peca_aleatoria, tabuleiro, coluna + 1, linha):
                            coluna += 1

                    # Se for apertado W, é atribuido o giro da peça na variável peca_girada, se não tiver colisão o giro é bem sucedido
                    if keyboard.is_pressed('w'):
                        peca_girada = girar_peca(peca_aleatoria)
                        if not colidir(peca_girada, tabuleiro, coluna, linha):
                            peca_aleatoria = peca_girada

                    # Se for apertado S, o tempo de queda é reduzido pela metade, acelerando a queda
                    if keyboard.is_pressed('s'):
                        tempo_queda = metade_tempo_queda
                    else:
                        tempo_queda = 0.5

                    # Caso não haja colisão, a peça vai caindo, sendo removido uma linha
                    if not colidir(peca_aleatoria, tabuleiro, coluna, linha + 1):
                        linha += 1
                    else:
                        # Caso haja colisão é printado uma nova peça, com todos os parametros sorteados de novo (tipo de pela, rotação e coluna)
                        print_peca(peca_aleatoria, tabuleiro, coluna, linha)
                        # Quando a peça para (colidiu), verifica se a peça era igual a bomba, se for, chama a função da bomba
                        if peca_aleatoria == bomba:
                            peca_bomba(tabuleiro)
                        if game_over(tabuleiro):
                            # Caso a função game_over seja True, ou seja, caso tenha alguma peça na linha 0, fim vira True e o programa sai desse loop
                            fim = True
                        peca_aleatoria = random.choice(pecas)
                        if random.choice([True, False]):
                            for x in range(random.randint(1, 3)):
                                peca_aleatoria = girar_peca(peca_aleatoria)
                        coluna = random.randint(1, 10 - len(peca_aleatoria[0]))
                        linha = 0

                    print_peca(peca_aleatoria, tabuleiro, coluna, linha)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    printar_tabuleiro(tabuleiro)
                    print(f"{pont} pontos.")
                    time.sleep(tempo_queda)

                # Caso a função game_over seja True, é printado fim de jogo e o usuário tem a opção de jogar novamente se quiser
                if game_over(tabuleiro):
                    print("\nFim de Jogo!")
                    jogar_novamente = input("Deseja jogar novamente? (S/N)").strip().upper()
                    # Verifica se foi digitado S ou N, se não for, fica em loop perguntando
                    while jogar_novamente not in ('S', 'N'):
                        jogar_novamente = input("Deseja jogar novamente? (S/N) ").strip().upper()
                    if jogar_novamente == "S":
                        # Caso o usuário queira jogar novamente, o terminal é limpo e retorna ao menu inicial
                        os.system('cls' if os.name == 'nt' else 'clear')
                    if jogar_novamente == "N":
                            fechar = True # Caso não queira jogar de novo, fechar vira True e o programa fecha
            case 2:
                # Chama a função print regras e depois que o usuário der enter no input da função limpa o terminal e volta pro menu inicial
                os.system('cls' if os.name == 'nt' else 'clear')
                print_regras()
                os.system('cls' if os.name == 'nt' else 'clear')
            case 3:
                # Se escolher sair, fechar é True e o programa fecha
                fechar = True

main()