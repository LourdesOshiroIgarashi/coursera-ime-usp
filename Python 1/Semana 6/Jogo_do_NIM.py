def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogadas? "))
    pecasrestantes = n
    pecasremovidas = 0
    print()
    if n % (m + 1) == 0:
        print("Voce começa!")
        print()
        while pecasrestantes > 0:
            inicio = usuario_escolhe_jogada(n, m)
            pecasrestantes = pecasrestantes - inicio
            n = pecasrestantes
            if pecasrestantes == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif pecasrestantes > 1:
                print("Agora restam {} peças no tabuleiro.".format(pecasrestantes))
            print()
            proximo = computador_escolhe_jogada(n, m)
            pecasrestantes = pecasrestantes - proximo
            n = pecasrestantes
    else:
        print("Computador começa!")
        print()
        while pecasrestantes > 0:
            inicio = computador_escolhe_jogada(n, m)
            pecasrestantes = pecasrestantes - inicio
            n = pecasrestantes
            if pecasrestantes == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif pecasrestantes != 0:
                print("Agora restam {} peças no tabuleiro.".format(pecasrestantes))
                print()
            if pecasrestantes != 0:
                proximo = usuario_escolhe_jogada(n, m)
                pecasremovidas = pecasremovidas + inicio + proximo
                pecasrestantes = pecasrestantes - proximo
                if pecasrestantes == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                elif pecasrestantes != 0:
                    print("Agora restam {} peças no tabuleiro.".format(pecasrestantes))
                print()
            n = pecasrestantes
    print("Fim do jogo! O computador ganhou!")
    print()


# Uma vez iniciado o jogo,
# a estratégia do computador para ganhar consiste em
# deixar sempre um número de peças que seja múltiplo de (m+1)
# ao jogador. Caso isso não seja possível,
# deverá tirar o número máximo de peças possíveis.
def computador_escolhe_jogada(n, m):
    if n > m and n % (m +1) == 0:
        pecasremovidas = n - m
    else:
        if n < m:
            pecasremovidas = n
        else:
            pecasremovidas = m
    if pecasremovidas == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou {} peças.".format(pecasremovidas))
    return pecasremovidas


def usuario_escolhe_jogada(n, m):
    pecasremovidas = int(input("Quantas peças você vai tirar? "))
    if pecasremovidas > m or pecasremovidas > n or pecasremovidas < 1:
        while pecasremovidas > m or pecasremovidas < 1:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
            pecasremovidas = int(input("Quantas peças você vai tirar? "))
    if pecasremovidas == 1:
        print()
        print("Voce tirou uma peça.".format(pecasremovidas))
    else:
        print("Voce tirou {} peças.".format(pecasremovidas))
    return pecasremovidas


def campeonato():
    print("**** Rodada 1 ****")
    print()
    a1 = partida()
    print("**** Rodada 2 ****")
    print()
    a2 = partida()
    print("**** Rodada 3 ****")
    print()
    a3 = partida()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")


print("Bem-vindo ao jogo do NIM! Escolha: ")
print()
print("1 - para jogar uma partida isolada")
x = int(input("2 - para jogar um campeonato "))
print()

if x == 1:
    print("Voce escolheu uma partida isolada!")
    print()
    jogo = partida()

elif x == 2:
    print("Voce escolheu um campeonato!")
    print()
    jogo = campeonato()
